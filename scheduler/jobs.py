import json
import os
import datetime
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.config import settings
from crawler.run_full_crawl import crawl_all
from db.mongo import init_mongo

log = logging.getLogger("scheduler")
_scheduler: AsyncIOScheduler | None = None


async def daily_job():
    # Run the crawl
    await crawl_all()

    # Summarize today's changes (UTC)
    db = await init_mongo()
    start = datetime.datetime.utcnow().date()
    start_dt = datetime.datetime.combine(start, datetime.time.min)

    cur = db.changes.find({"ts": {"$gte": start_dt}})
    changes = [c async for c in cur]

    # Persist report
    os.makedirs(settings.REPORT_BUCKET, exist_ok=True)
    path = os.path.join(settings.REPORT_BUCKET, f"changes_{start}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(changes, f, default=str, ensure_ascii=False, indent=2)

    log.info("Daily report written to %s (%d change(s))", path, len(changes))


def start_scheduler():
    """Start an in-process APScheduler on the current asyncio loop."""
    if not getattr(settings, "SCHEDULER_ENABLED", True):
        log.info("Scheduler disabled by config")
        return None

    global _scheduler
    if _scheduler and _scheduler.running:
        return _scheduler

    _scheduler = AsyncIOScheduler(timezone="UTC")
    # Run every day at 01:00 UTC
    _scheduler.add_job(daily_job, "cron", hour=1, minute=0, id="daily_job", replace_existing=True)
    _scheduler.start()
    log.info("Scheduler started")
    return _scheduler


def stop_scheduler():
    global _scheduler
    if _scheduler and _scheduler.running:
        _scheduler.shutdown(wait=False)
        log.info("Scheduler stopped")
        _scheduler = None
