# api/main.py
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from api.routers import books, changes
from api.rate_limit import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from utils.logging import setup_logging
from utils.config import settings
from db.mongo import init_mongo
from scheduler.jobs import start_scheduler

app = FastAPI(title="Books API", version="1.0.0")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def ratelimit_handler(request: Request, exc: RateLimitExceeded):
    return PlainTextResponse(str(exc.detail), status_code=429)

app.include_router(books.router)
app.include_router(changes.router)

@app.on_event("startup")
async def on_startup():
    setup_logging(settings.LOG_LEVEL)
    await init_mongo()
    start_scheduler()
