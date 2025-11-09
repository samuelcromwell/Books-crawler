async def ensure_indexes(db):
    await db.books.create_index("product_url", unique=True)
    await db.books.create_index([("category",1), ("rating",-1), ("price_incl_tax",1)])
    await db.changes.create_index([("ts",-1)])
    await db.crawl_state.create_index("scope", unique=True)
