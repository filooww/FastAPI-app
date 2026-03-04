# 🛒 Shop API (FastAPI)

A modern, asynchronous REST API for an e-commerce platform built with **FastAPI** and **SQLAlchemy 2.0**.

## 🚀 Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous)
* **Database:** SQLite (via [aiosqlite](https://github.com/omnilib/aiosqlite))
* **ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (Async Engine)
* **Dependency Management:** [Poetry](https://python-poetry.org/)
* **Web Server:** Uvicorn

## 🛠 Key Features

* **Fully Asynchronous:** Non-blocking database operations and request handling.
* **Modern ORM:** Leveraging SQLAlchemy 2.0's 2.0-style syntax and async sessions.
* **Lifespan Management:** Automatic database table creation on application startup.
* **Scalable Structure:** Organized using API routers, centralized configuration, and dedicated models.
* **Validation:** Robust data validation and serialization using Pydantic.

## 📦 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/shop-api.git](https://github.com/YOUR_USERNAME/shop-api.git)
cd shop-api

2. Install dependencies

Make sure you have Poetry installed.
Bash

poetry install

3. Run the application
Bash

poetry run uvicorn main:app --reload

The API will be available at: http://127.0.0.1:8000
📑 API Documentation

Once the server is running, you can explore the API through:

    Swagger UI: http://127.0.0.1:8000/docs — Interactive API testing.

    ReDoc: http://127.0.0.1:8000/redoc — Detailed schema documentation.

🏗 Project Structure
Plaintext

.
├── api_v1/         # API endpoints (version 1)
├── core/           # Core logic and configuration
│   ├── models/     # SQLAlchemy models & DB helper
│   └── config.py   # Application settings
├── main.py         # Application entry point & lifespan
├── pyproject.toml  # Project dependencies and metadata
└── db.sqlite3      # Database file (auto-generated)
