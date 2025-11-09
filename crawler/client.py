import httpx
from contextlib import asynccontextmanager
from backoff import expo, on_exception
from typing import AsyncGenerator

DEFAULT_HEADERS = {"User-Agent": "books-crawler/1.0 (+https://example.com)"}

# Retry policy: retry on network errors and 429/5xx; do NOT retry most 4xx.
def _giveup(exc: Exception) -> bool:
    if isinstance(exc, httpx.HTTPStatusError):
        code = exc.response.status_code
        # Give up on client errors except 429 (too many requests)
        return 400 <= code < 500 and code != 429
    return False

@asynccontextmanager
async def get_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    timeout = httpx.Timeout(connect=10.0, read=25.0, write=10.0, pool=10.0)
    limits = httpx.Limits(max_keepalive_connections=20, max_connections=100)
    async with httpx.AsyncClient(
        headers=DEFAULT_HEADERS,
        http2=True,
        timeout=timeout,
        limits=limits,
        follow_redirects=True,
    ) as c:
        yield c

@on_exception(
    expo,
    (httpx.RequestError, httpx.HTTPStatusError),
    max_tries=5,
    giveup=_giveup,
    jitter=None,
)
async def fetch(client: httpx.AsyncClient, url: str) -> str:
    r = await client.get(url)
    # Raise for status so HTTP 4xx/5xx become HTTPStatusError (handled by backoff)
    r.raise_for_status()
    return r.text
