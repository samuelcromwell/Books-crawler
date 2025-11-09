import asyncio
import logging
from urllib.parse import urljoin

from utils.config import settings
from utils.logging import setup_logging
from utils.hashing import make_fingerprint
from db.mongo import init_mongo
from db.indexes import ensure_indexes
from crawler.client import get_client, fetch
from crawler.parser import parse_book_page

log = logging.getLogger("crawl")


async def iter_category_pages(client, start_url):
    url = start_url
    from selectolax.parser import HTMLParser

    while url:
        html = await fetch(client, url)
        yield url, html
        # find next page
        t = HTMLParser(html)
        nxt = t.css_first("li.next a")
        url = urljoin(url, nxt.attributes["href"]) if nxt else None


async def parse_listing_for_book_links(html, page_url):
    from selectolax.parser import HTMLParser
    t = HTMLParser(html)
    for a in t.css("article.product_pod h3 a"):
        href = a.attributes["href"]
        # Let urljoin resolve the ../../../ segments to /catalogue/...
        yield urljoin(page_url, href)

async def upsert_book(db, data: dict) -> str:
    now = __import__("datetime").datetime.utcnow()

    # Compute a stable fingerprint BEFORE adding transient fields
    content_hash = make_fingerprint(data)

    # Fill/refresh bookkeeping fields
    data = dict(data)  # shallow copy to avoid mutating caller
    data["content_hash"] = content_hash
    data["updated_at"] = now
    data["crawl_meta"] = {"ts": now, "status": "ok", "source_url": data["product_url"]}

    # Check existing
    existing = await db.books.find_one({"product_url": data["product_url"]}, {"_id": 1, "content_hash": 1, "created_at": 1})
    if not existing:
        data.setdefault("created_at", now)
        await db.books.insert_one(data)
        await db.changes.insert_one(
            {
                "product_url": data["product_url"],
                "change_type": "create",
                "changed_fields": {},
                "ts": now,
            }
        )
        return "created"

    # Existing doc: preserve original created_at
    old_doc = await db.books.find_one({"_id": existing["_id"]})
    data["created_at"] = old_doc.get("created_at", now)

    if existing.get("content_hash") != content_hash:
        # compute changed fields (simple diff, only across keys present in new data)
        changed = {
            k: {"old": old_doc.get(k), "new": data.get(k)}
            for k in data.keys()
            if old_doc.get(k) != data.get(k)
        }
        await db.books.replace_one({"_id": old_doc["_id"]}, data)
        await db.changes.insert_one(
            {
                "product_url": data["product_url"],
                "change_type": "update",
                "changed_fields": changed,
                "ts": now,
            }
        )
        return "updated"

    return "skipped"


async def crawl_all():
    setup_logging()
    db = await init_mongo()
    await ensure_indexes(db)

    base = settings.BASE_URL.rstrip("/")
    start = urljoin(base + "/", "/")

    from selectolax.parser import HTMLParser

    async with get_client() as client:
        # 1) discover categories
        home = await fetch(client, start)
        t = HTMLParser(home)
        cat_links = [
            urljoin(base + "/", a.attributes["href"])
            for a in t.css("ul.nav-list ul li a")
        ]
        log.info("Found %d categories", len(cat_links))

        # 2) iterate every category page
        for cat_url in cat_links:
            async for page_url, page_html in iter_category_pages(client, cat_url):
                # 3) book links in this page
                async for book_url in parse_listing_for_book_links(page_html, page_url):
                    # 4) fetch product page
                    try:
                        page = await fetch(client, book_url)
                        data = parse_book_page(page, book_url)
                        status = await upsert_book(db, data)
                        log.info("[%s] %s", status, data.get("name", "(unknown title)"))
                    except Exception as e:
                        log.exception("Failed book %s: %s", book_url, e)


if __name__ == "__main__":
    asyncio.run(crawl_all())
