# scheduler/jobs.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.config import settings
from crawler.run_full_crawl import crawl_all
from db.mongo import init_mongo
import json, os, datetime, logging

log = logging.getLogger("scheduler")

async def daily_job():
    # 1) crawl (handles upserts + changelog)
    await crawl_all()

    # 2) emit today's change report
    db = await init_mongo()
    start = datetime.datetime.utcnow().date()
    start_dt = datetime.datetime.combine(start, datetime.time.min)
    cur = db.changes.find({"ts": {"$gte": start_dt}})
    changes = [c async for c in cur]

    os.makedirs(settings.REPORT_BUCKET, exist_ok=True)
    path = os.path.join(settings.REPORT_BUCKET, f"changes_{start}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(changes, f, default=str, ensure_ascii=False, indent=2)

    log.info("Daily report written to %s (%d change(s))", path, len(changes))

def start_scheduler():
    """Start an in-process APScheduler on the current asyncio loop."""
    if not settings.SCHEDULER_ENABLED:
        log.info("Scheduler disabled by config")
        return
    sched = AsyncIOScheduler(timezone="UTC")
    # daily at 01:00 UTC (adjust as needed)
    sched.add_job(daily_job, "cron", hour=1, minute=0)
    sched.start()
    log.info("Scheduler started")
