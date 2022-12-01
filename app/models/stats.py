from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId
from app.models.classes import LabsSchema
import uuid
from enum import Enum

class Report(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    address: str
    report: str
    timestamp: datetime

    class Config:
        schema_extra = {
            "example": {
                "email": "0x0eb638648207d00b9025684d13b1cb53806debe4",
                "report": "...",
                "timestamp": "2021-09-01T00:00:00",
            }
        }
