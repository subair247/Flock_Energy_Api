# Flock Energy - Urja Meter Ops API Service

A clean, modern REST API proxy wrapper built over the legacy internal web portal ("Urja Meter Ops"). This service automates authentication, session cookie management, and HTML scraping to expose structured, programmatic JSON data for downstream clients.

---

## Project Structure

```text
flock-energy-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point & API route definitions
│   ├── client.py        # Legacy Urja Portal HTTP adapter & scraper logic
│   ├── models.py        # Pydantic data validation schemas
│   └── config.py        # Environment settings & configuration
├── openapi.json         # Exported OpenAPI 3.0 specification
├── PROTOCOL.md          # Documentation of legacy portal behavior
├── REFLECTION.md        # Assignment reflection responses
├── README.md            # Main documentation and setup guide
└── requirements.txt     # Python project dependencies