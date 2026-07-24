from fastapi import FastAPI, HTTPException
from app.client import UrjaPortalClient
from app.models import MeterResponse
from app.config import settings

app = FastAPI(
    title="Flock Energy - Urja Meter Ops API",
    version="1.0.0",
    description="Clean REST API proxy wrapper over the legacy Urja Meter Ops portal."
)

portal_client = UrjaPortalClient(settings.base_url)

@app.get("/api/v1/meters/{meter_id}", response_model=MeterResponse)
def get_meter(meter_id: str):
    try:
        data = portal_client.get_meter_details(meter_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}