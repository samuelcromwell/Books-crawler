from selectolax.parser import HTMLParser

RATING_MAP = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

def parse_book_page(html: str, url: str) -> dict:
    tree = HTMLParser(html)

    name = tree.css_first("div.product_main h1").text(strip=True)
    # rating from class 'star-rating Three'
    rating_cls = tree.css_first("p.star-rating").attributes.get("class","")
    rating = next((RATING_MAP[w] for w in rating_cls.split() if w in RATING_MAP), None)

    # product table (UPC, prices, availability, reviews)
    table = { row.css_first("th").text(): row.css_first("td").text()
              for row in tree.css("table.table.table-striped tr") }

    upc = table.get("UPC")
    price_excl = table.get("Price (excl. tax)", "").replace("£","").strip()
    price_incl = table.get("Price (incl. tax)", "").replace("£","").strip()
    tax = table.get("Tax","")
    availability = table.get("Availability","")  # parse number if present
    num_reviews = int(table.get("Number of reviews","0"))

    # description is the next sibling after #product_description
    desc_hdr = tree.css_first("#product_description")
    description = ""
    if desc_hdr:
        p = desc_hdr.parent.next_sibling
        if p: description = p.text(strip=True)

    # category from breadcrumb: "Books > Fiction > ..."
    bc = tree.css("ul.breadcrumb li a")
    category = bc[-1].text(strip=True) if len(bc) >= 3 else "Books"

    img = tree.css_first("div.item.active img")
    image_url = img.attributes.get("src","").replace("../../", "https://books.toscrape.com/")

    return {
        "product_url": url,
        "upc": upc,
        "name": name,
        "description": description,
        "category": category,
        "price_incl_tax": float(price_incl or 0.0),
        "price_excl_tax": float(price_excl or 0.0),
        "availability": availability,
        "num_reviews": num_reviews,
        "image_url": image_url,
        "rating": rating,
        "raw_html": html
    }
