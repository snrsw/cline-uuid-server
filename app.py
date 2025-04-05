from fastapi import FastAPI, Query, HTTPException
from typing import List, Dict, Union, Optional, Annotated
from pydantic import BaseModel, Field
import uuid
from uuid import UUID

app: FastAPI = FastAPI(
    title="UUID4 Generator API",
    description="A simple API that generates UUID4 values",
    version="0.1.0"
)

class UUIDResponse(BaseModel):
    """Response model for a single UUID"""
    uuid: str = Field(..., description="A UUID4 string")

class BatchUUIDResponse(BaseModel):
    """Response model for multiple UUIDs"""
    uuids: List[str] = Field(..., description="List of UUID4 strings")

@app.get("/uuid", response_model=None, response_description="A UUID4 string")
async def get_uuid() -> str:
    """Generate and return a single UUID4 as plain text

    Returns:
        str: A UUID4 string
    """
    return str(uuid.uuid4())

@app.get("/uuid/json", response_model=UUIDResponse, response_description="UUID in JSON format")
async def get_uuid_json() -> UUIDResponse:
    """Generate and return a single UUID4 in JSON format

    Returns:
        UUIDResponse: Object containing a UUID4 string
    """
    return UUIDResponse(uuid=str(uuid.uuid4()))

@app.get("/uuid/batch", response_model=BatchUUIDResponse, response_description="Multiple UUIDs in JSON format")
async def get_batch_uuids(
    count: Annotated[int, Query(ge=1, le=100, description="Number of UUIDs to generate")] = 1
) -> BatchUUIDResponse:
    """Generate and return multiple UUID4 values

    Args:
        count: Number of UUIDs to generate (1-100)

    Returns:
        BatchUUIDResponse: Object containing a list of UUID4 strings
    """
    uuids: List[str] = [str(uuid.uuid4()) for _ in range(count)]
    return BatchUUIDResponse(uuids=uuids)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
