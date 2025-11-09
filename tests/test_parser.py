import pytest
from crawler.parser import parse_book_page

def test_parse_minimal(sample_html):
    doc = parse_book_page(sample_html, "https://books.toscrape.com/cat/book_1")
    assert doc["name"]
    assert 0 <= doc["price_incl_tax"]
