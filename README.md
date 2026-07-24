# Flock Energy - Urja Meter Ops API Service

A clean, modern REST API proxy wrapper built over the legacy internal web portal ("Urja Meter Ops"). This service automates authentication, session cookie management, and HTML scraping to expose structured, programmatic JSON data for downstream clients.

---

## Project Structure

flock-energy-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point & API route definitions
│   ├── client.py        # Legacy Urja Portal HTTP adapter & scraper logic
│   ├── models.py        # Pydantic data validation schemas
│   └── config.py        # Environment settings & configuration
├── openapi.json         # Exported OpenAPI 3.0 specification
├── PROTOCOL.md          # Documentation of legacy portal behavior
├── REFLECTION.md        # Assignment reflection responses
├── README.md            # Main documentation and setup guide
└── requirements.txt     # Python project dependencies

---

Installation & Running Locally
Prerequisites
Python 3.10 or higher installed on your machine.

---

Setup Instructions
1.Clone or download the repository and navigate into the project directory:

cd flock-energy-api

---

2.Create and activate a Python virtual environment:

python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

3.Install dependencies:

pip install -r requirements.txt

4.Start the application using Uvicorn:

uvicorn app.main:app --reload --port 8000

The API will now be running locally at http://localhost:8000. You can access the interactive Swagger documentation UI directly at http://localhost:8000/docs