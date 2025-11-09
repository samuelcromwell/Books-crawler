import hashlib, json

STABLE_FIELDS = ["name","description","category","price_incl_tax","price_excl_tax",
                 "availability","num_reviews","image_url","rating"]

def make_fingerprint(doc: dict) -> str:
    payload = {k: doc.get(k) for k in STABLE_FIELDS}
    s = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()
