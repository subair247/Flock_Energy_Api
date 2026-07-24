from pydantic import BaseModel, Field

class MeterResponse(BaseModel):
    meter_id: str = Field(..., description="Unique internal identifier of the meter")
    serial_number: str = Field(..., description="Physical serial number of the smart meter")
    status: str = Field(..., description="Operational status (e.g., ACTIVE, INACTIVE)")
    location: str = Field(..., description="Network node location hierarchy string")