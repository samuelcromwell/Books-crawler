# 📚 Books Crawler – Production-Grade Web Scraping and REST API

A robust, asynchronous Python project designed to crawl [books.toscrape.com](https://books.toscrape.com), store normalized data in MongoDB, detect daily changes, and serve the results over a secure FastAPI REST API with comprehensive features like filtering, pagination, authentication, and rate-limiting.

This README provides all necessary information for running the project locally or in Docker, configuration, testing, and extension.

---

## ✨ Features

* **Async & Fast:** Uses **httpx** and **HTTP/2** for high-speed, concurrent crawling.
* **Resilient:** Includes **exponential backoff**, robust error handling, and tolerance for unexpected DOM structure.
* **Change Detection:** **Content fingerprinting** is used to accurately detect changes (e.g., price, availability, description) between crawls.
* **Scheduled Updates:** An **APScheduler** runs a daily crawl and generates **JSON change reports**.
* **Data Storage:** Stores normalized book data in **MongoDB** (NoSQL), including **raw HTML snapshots** for auditing or fallback parsing.
* **Secure REST API:** A **FastAPI** server provides **API key authentication**, **rate limiting**, advanced filtering, sorting, and pagination.
* **Production-Ready:** Structured logging, Pydantic schemas, MongoDB indexes, and configuration via `.env`.

---

## 🏗️ Architecture

| Component | Description | Technologies |
| :--- | :--- | :--- |
| **Crawler** | Discovers pages, extracts data, and upserts into MongoDB. | `httpx` (async), `selectolax` (HTML parsing) |
| **Scheduler** | Runs the full crawl/change detection job daily and generates reports. | `APScheduler` |
| **API** | Securely exposes book data and change logs. | `FastAPI`, `Uvicorn` |
| **Database** | Persistent storage for books and change records. | `MongoDB`, `motor` (async driver) |

### API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/books` | Retrieve books with filters, pagination, and sorting. |
| `GET` | `/books/{id}` | Get detailed information for a specific book. |
| `GET` | `/changes` | View recent change logs, filterable by date and URL. |

---

## 🛠️ Tech Stack

* **Python:** 3.11+
* **Web Framework:** FastAPI, Uvicorn
* **Async HTTP:** httpx
* **HTML Parsing:** selectolax
* **Data Validation:** Pydantic
* **Database:** MongoDB (via motor)
* **Scheduling:** APScheduler
* **Retry Logic:** backoff
* **Deployment:** Docker / Docker Compose (Optional)

---

## 📁 Directory Structure

```text
.
├─ crawler/             # Core scraping logic
│  ├─ client.py         # Async HTTP client + retry logic
│  ├─ parser.py         # HTML parsing and data normalization
│  └─ run_full_crawl.py # Crawler entrypoint
├─ scheduler/           # Daily job management and reporting
│  └─ jobs.py           # Scheduler setup and daily task
├─ api/                 # FastAPI application and schemas
│  ├─ main.py           # Endpoints, Auth, Rate Limits
│  └─ schemas.py        # Pydantic models for API data
├─ db/                  # Database connections and setup
│  ├─ mongo.py          # MongoDB connection initialization
│  └─ indexes.py        # Index creation
├─ utils/               # Shared utilities
│  ├─ config.py         # Environment configuration (BaseSettings)
│  ├─ hashing.py        # Content fingerprinting
│  └─ logging.py        # Structured logging setup
├─ tests/               # Unit/Integration tests
├─ docker/              # Dockerfile(s) / compose files
├─ README.md
└─ requirements.txt

I'd be happy to rewrite and refine the provided text into a clean, structured README.md format using Markdown.

Here is the refined content:

Markdown

# 📚 Books Crawler – Production-Grade Web Scraping and REST API

A robust, asynchronous Python project designed to crawl [books.toscrape.com](https://books.toscrape.com), store normalized data in MongoDB, detect daily changes, and serve the results over a secure FastAPI REST API with comprehensive features like filtering, pagination, authentication, and rate-limiting.

This README provides all necessary information for running the project locally or in Docker, configuration, testing, and extension.

---

## ✨ Features

* **Async & Fast:** Uses **httpx** and **HTTP/2** for high-speed, concurrent crawling.
* **Resilient:** Includes **exponential backoff**, robust error handling, and tolerance for unexpected DOM structure.
* **Change Detection:** **Content fingerprinting** is used to accurately detect changes (e.g., price, availability, description) between crawls.
* **Scheduled Updates:** An **APScheduler** runs a daily crawl and generates **JSON change reports**.
* **Data Storage:** Stores normalized book data in **MongoDB** (NoSQL), including **raw HTML snapshots** for auditing or fallback parsing.
* **Secure REST API:** A **FastAPI** server provides **API key authentication**, **rate limiting**, advanced filtering, sorting, and pagination.
* **Production-Ready:** Structured logging, Pydantic schemas, MongoDB indexes, and configuration via `.env`.

---

## 🏗️ Architecture

| Component | Description | Technologies |
| :--- | :--- | :--- |
| **Crawler** | Discovers pages, extracts data, and upserts into MongoDB. | `httpx` (async), `selectolax` (HTML parsing) |
| **Scheduler** | Runs the full crawl/change detection job daily and generates reports. | `APScheduler` |
| **API** | Securely exposes book data and change logs. | `FastAPI`, `Uvicorn` |
| **Database** | Persistent storage for books and change records. | `MongoDB`, `motor` (async driver) |

### API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/books` | Retrieve books with filters, pagination, and sorting. |
| `GET` | `/books/{id}` | Get detailed information for a specific book. |
| `GET` | `/changes` | View recent change logs, filterable by date and URL. |

---

## 🛠️ Tech Stack

* **Python:** 3.11+
* **Web Framework:** FastAPI, Uvicorn
* **Async HTTP:** httpx
* **HTML Parsing:** selectolax
* **Data Validation:** Pydantic
* **Database:** MongoDB (via motor)
* **Scheduling:** APScheduler
* **Retry Logic:** backoff
* **Deployment:** Docker / Docker Compose (Optional)

---

## 📁 Directory Structure

```text
.
├─ crawler/             # Core scraping logic
│  ├─ client.py         # Async HTTP client + retry logic
│  ├─ parser.py         # HTML parsing and data normalization
│  └─ run_full_crawl.py # Crawler entrypoint
├─ scheduler/           # Daily job management and reporting
│  └─ jobs.py           # Scheduler setup and daily task
├─ api/                 # FastAPI application and schemas
│  ├─ main.py           # Endpoints, Auth, Rate Limits
│  └─ schemas.py        # Pydantic models for API data
├─ db/                  # Database connections and setup
│  ├─ mongo.py          # MongoDB connection initialization
│  └─ indexes.py        # Index creation
├─ utils/               # Shared utilities
│  ├─ config.py         # Environment configuration (BaseSettings)
│  ├─ hashing.py        # Content fingerprinting
│  └─ logging.py        # Structured logging setup
├─ tests/               # Unit/Integration tests
├─ docker/              # Dockerfile(s) / compose files
├─ README.md
└─ requirements.txt

```

🚀 Quick Start
1. Prerequisites
MongoDB (local instance or remote connection).

Python 3.11+ (for local development) or Docker (for containerized run).

2. Environment Variables
Create a .env file in the project root:

```
# Target site
BASE_URL=[https://books.toscrape.com](https://books.toscrape.com)

# Mongo Connection
MONGO_URI=mongodb://mongo:27017
MONGO_DB=booksdb

# API Settings
API_HOST=0.0.0.0
API_PORT=8000
API_KEY=supersecretapikey

# Rate limiting (per API_KEY)
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW_SECONDS=3600

# Scheduler
SCHEDULER_ENABLED=true
REPORT_BUCKET=/reports

# Logging
LOG_LEVEL=INFO
```

I'd be happy to rewrite and refine the provided text into a clean, structured README.md format using Markdown.

Here is the refined content:

Markdown

# 📚 Books Crawler – Production-Grade Web Scraping and REST API

A robust, asynchronous Python project designed to crawl [books.toscrape.com](https://books.toscrape.com), store normalized data in MongoDB, detect daily changes, and serve the results over a secure FastAPI REST API with comprehensive features like filtering, pagination, authentication, and rate-limiting.

This README provides all necessary information for running the project locally or in Docker, configuration, testing, and extension.

---

## ✨ Features

* **Async & Fast:** Uses **httpx** and **HTTP/2** for high-speed, concurrent crawling.
* **Resilient:** Includes **exponential backoff**, robust error handling, and tolerance for unexpected DOM structure.
* **Change Detection:** **Content fingerprinting** is used to accurately detect changes (e.g., price, availability, description) between crawls.
* **Scheduled Updates:** An **APScheduler** runs a daily crawl and generates **JSON change reports**.
* **Data Storage:** Stores normalized book data in **MongoDB** (NoSQL), including **raw HTML snapshots** for auditing or fallback parsing.
* **Secure REST API:** A **FastAPI** server provides **API key authentication**, **rate limiting**, advanced filtering, sorting, and pagination.
* **Production-Ready:** Structured logging, Pydantic schemas, MongoDB indexes, and configuration via `.env`.

---

## 🏗️ Architecture

| Component | Description | Technologies |
| :--- | :--- | :--- |
| **Crawler** | Discovers pages, extracts data, and upserts into MongoDB. | `httpx` (async), `selectolax` (HTML parsing) |
| **Scheduler** | Runs the full crawl/change detection job daily and generates reports. | `APScheduler` |
| **API** | Securely exposes book data and change logs. | `FastAPI`, `Uvicorn` |
| **Database** | Persistent storage for books and change records. | `MongoDB`, `motor` (async driver) |

### API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/books` | Retrieve books with filters, pagination, and sorting. |
| `GET` | `/books/{id}` | Get detailed information for a specific book. |
| `GET` | `/changes` | View recent change logs, filterable by date and URL. |

### API reference example commands
```
export API_KEY="<your-new-key>"

# list, pretty-print
curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books?page=1&page_size=10" | python -m json.tool

# filter + price range + sort by price
curl -s -H "X-API-Key: $API_KEY" \
  "http://localhost:9010/books?category=Mystery&min_price=10&max_price=30&sort_by=price&page=1&page_size=10" \
  | python -m json.tool

# sort by rating
curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books?sort_by=rating&page=1&page_size=5" | python -m json.tool

# get one book by id
BOOK_ID=$(
  curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books?page=1&page_size=1" \
  | python -c 'import sys,json; print(json.load(sys.stdin)["items"][0]["id"])'
)
curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books/$BOOK_ID" | python -m json.tool

```
---

## 🛠️ Tech Stack

* **Python:** 3.11+
* **Web Framework:** FastAPI, Uvicorn
* **Async HTTP:** httpx
* **HTML Parsing:** selectolax
* **Data Validation:** Pydantic
* **Database:** MongoDB (via motor)
* **Scheduling:** APScheduler
* **Retry Logic:** backoff
* **Deployment:** Docker / Docker Compose (Optional)

---

## 📁 Directory Structure

```text
.
├─ crawler/             # Core scraping logic
│  ├─ client.py         # Async HTTP client + retry logic
│  ├─ parser.py         # HTML parsing and data normalization
│  └─ run_full_crawl.py # Crawler entrypoint
├─ scheduler/           # Daily job management and reporting
│  └─ jobs.py           # Scheduler setup and daily task
├─ api/                 # FastAPI application and schemas
│  ├─ main.py           # Endpoints, Auth, Rate Limits
│  └─ schemas.py        # Pydantic models for API data
├─ db/                  # Database connections and setup
│  ├─ mongo.py          # MongoDB connection initialization
│  └─ indexes.py        # Index creation
├─ utils/               # Shared utilities
│  ├─ config.py         # Environment configuration (BaseSettings)
│  ├─ hashing.py        # Content fingerprinting
│  └─ logging.py        # Structured logging setup
├─ tests/               # Unit/Integration tests
├─ docker/              # Dockerfile(s) / compose files
├─ README.md
└─ requirements.txt

```

🚀 Quick Start
1. Prerequisites
MongoDB (local instance or remote connection).

Python 3.11+ (for local development) or Docker (for containerized run).

2. Environment Variables
Create a .env file in the project root:

```
# Target site
BASE_URL=[https://books.toscrape.com](https://books.toscrape.com)

# Mongo Connection
MONGO_URI=mongodb://mongo:27017
MONGO_DB=booksdb

# API Settings
API_HOST=0.0.0.0
API_PORT=8000
API_KEY=supersecretapikey

# Rate limiting (per API_KEY)
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW_SECONDS=3600

# Scheduler
SCHEDULER_ENABLED=true
REPORT_BUCKET=/reports

# Logging
LOG_LEVEL=INFO
Tip: Use a strong API_KEY in production.

```

3. Run with Docker Compose
docker-compose.yml is present to launch the app and MongoDB services:

```

docker compose up -d --build
API URL: http://localhost:8000

Swagger UI: http://localhost:8000/docs

```

4. Run Locally (Development)

```
# Setup virtual environment
python -m venv .venv && source .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run the crawler once
python -m crawler.run_full_crawl
# Start the API server
uvicorn api.main:app --host ${API_HOST:-0.0.0.0} --port ${API_PORT:-8000} --reload

```

## Database Schema

### Books Collection

Example document (trimmed):

```
{
  "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
  "name": "A Light in the Attic",
  "category": "Poetry",
  "price_incl_tax": "£51.77",
  "price_excl_tax": "£51.77",
  "availability": "In stock (22 available)",
  "num_reviews": 0,
  "image_url": "https://books.toscrape.com/media/cache/xx.jpg",
  "rating": 3,
  "description": "It's hard to pick one thing to like...",
  "upc": "A123456789",
  "raw_html": "<!doctype html> ...",
  "content_hash": "1a5c...e9",
  "created_at": "2025-11-09T20:24:21.498Z",
  "updated_at": "2025-11-09T20:24:21.498Z",
  "crawl_meta": {
    "ts": "2025-11-09T20:24:21.498Z",
    "status": "ok",
    "source_url": "https://books.toscrape.com/catalogue/..."
  }
}

```

## Changes Collection
### Example Document

```
{
  "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
  "change_type": "update",
  "changed_fields": {
    "price_incl_tax": { "old": "£51.77", "new": "£49.99" },
    "availability":   { "old": "In stock (22 available)", "new": "In stock (20 available)" }
  },
  "ts": "2025-11-10T01:02:00.100Z"
}

```

### Commands
The Commands.md file shows the various specific API calls and their responses

### Screenshots
Screenshots of successful crawl runs and scheduler runs are attached in images folder

## License & Acknowledgements

For demonstration/assessment purposes.

Data source: Books to Scrape
 — a learning site.

# © Samuel Cromwell.