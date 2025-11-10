from selectolax.parser import HTMLParser
from urllib.parse import urljoin

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
BASE = "https://books.toscrape.com/"

def _abs(src: str) -> str:
    # books.toscrape uses relative paths like ../../media/...
    return urljoin(BASE, src or "")

def _parse_availability(text: str) -> int:
    # e.g. "In stock (22 available)" -> 22; return 0 if no number
    import re
    m = re.search(r"(\d+)", text or "")
    return int(m.group(1)) if m else 0

def parse_book_page(html: str, url: str) -> dict:
    tree = HTMLParser(html)

    # Name
    name_node = tree.css_first("div.product_main h1")
    name = name_node.text(strip=True) if name_node else None

    # Rating (class e.g., 'star-rating Three')
    rating_node = tree.css_first("p.star-rating")
    rating = None
    if rating_node:
        cls = (rating_node.attributes.get("class") or "").split()
        rating = next((RATING_MAP.get(w) for w in cls if w in RATING_MAP), None)

    # Product table (UPC, prices, availability, reviews)
    table_rows = tree.css("table.table.table-striped tr")
    table = {}
    for row in table_rows:
        th = row.css_first("th")
        td = row.css_first("td")
        if th and td:
            table[th.text(strip=True)] = td.text(strip=True)

    upc = table.get("UPC")
    price_excl = (table.get("Price (excl. tax)") or "").replace("£", "").replace(",", "").strip()
    price_incl = (table.get("Price (incl. tax)") or "").replace("£", "").replace(",", "").strip()
    availability_txt = table.get("Availability") or ""
    availability = _parse_availability(availability_txt)
    num_reviews = int((table.get("Number of reviews") or "0").strip() or 0)

    # Description: <div id="product_description"> ... </div> followed by the <p>
    description = ""
    if tree.css_first("#product_description"):
        # adjacent sibling <p>
        desc_p = tree.css_first("#product_description + p") or tree.css_first("#product_description ~ p")
        if desc_p:
            description = desc_p.text().strip()

    # Category from breadcrumb anchors: Home > Books > <Category> > (active title)
    # The last <a> is the category (active title is not an <a>)
    bc_links = tree.css("ul.breadcrumb li a")
    category = bc_links[-1].text(strip=True) if bc_links else "Books"

    # Image URL (make absolute)
    img = tree.css_first("div.item.active img") or tree.css_first(".thumbnail img")
    image_url = _abs(img.attributes.get("src", "")) if img else ""

    return {
        "product_url": url,              # keep this name if your DB/index expects it
        "upc": upc,
        "name": name,
        "description": description,
        "category": category,
        "price_incl_tax": float(price_incl or 0.0),
        "price_excl_tax": float(price_excl or 0.0),
        "availability": availability,    # normalized to int count
        "num_reviews": num_reviews,
        "image_url": image_url,
        "rating": rating,
        "raw_html": html,
    }
