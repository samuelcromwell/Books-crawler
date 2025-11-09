import httpx
from contextlib import asynccontextmanager
from backoff import expo, on_exception

DEFAULT_HEADERS = {"User-Agent": "books-crawler/1.0 (+https://example.com)"}

@asynccontextmanager
async def get_client():
    async with httpx.AsyncClient(headers=DEFAULT_HEADERS, http2=True, timeout=30) as c:
        yield c

@on_exception(expo, (httpx.RequestError, httpx.ReadTimeout), max_tries=5)
async def fetch(client: httpx.AsyncClient, url: str) -> str:
    r = await client.get(url)
    r.raise_for_status()
    return r.text
