# Inventory API

A product inventory management REST API built with FastAPI and PostgreSQL.

## Features
- Add, update, delete and view products
- PostgreSQL database integration
- Deployed on Render with custom domain

## Tech Stack
- Python, FastAPI, PostgreSQL, SQLAlchemy, Render

## Run Locally

1. Clone the repo
   git clone https://github.com/heyyojas/inventory-api

2. Install dependencies
   pip install -r requirements.txt

3. Set up environment variables
   DATABASE_URL=your_postgresql_url

4. Run the server
   uvicorn main:app --reload

## Note
Free tier database may be spun down. Clone and run locally for full functionality.
