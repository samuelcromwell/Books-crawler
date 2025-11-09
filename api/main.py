from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.openapi.utils import get_openapi
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from api.routers import books, changes
from api.rate_limit import limiter
from utils.logging import setup_logging
from utils.config import settings
from db.mongo import init_mongo, close_mongo
from scheduler.jobs import start_scheduler

def create_app() -> FastAPI:
    app = FastAPI(title="Books API", version="1.0.0")
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)

    # OpenAPI: add ApiKeyAuth so Swagger shows "Authorize"
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        schema = get_openapi(title=app.title, version=app.version, routes=app.routes)
        comp = schema.setdefault("components", {})
        sec = comp.setdefault("securitySchemes", {})
        sec["ApiKeyAuth"] = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
        schema["security"] = [{"ApiKeyAuth": []}]
        app.openapi_schema = schema
        return schema

    app.openapi = custom_openapi

    @app.exception_handler(RateLimitExceeded)
    def ratelimit_handler(request: Request, exc: RateLimitExceeded):
        return PlainTextResponse(str(exc.detail), status_code=429)

    app.include_router(books.router)
    app.include_router(changes.router)
    return app

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    setup_logging(settings.LOG_LEVEL)
    await init_mongo()
    start_scheduler()  # <-- no loop argument
    try:
        yield
    finally:
        await close_mongo()

app = create_app()
app.router.lifespan_context = lifespan
