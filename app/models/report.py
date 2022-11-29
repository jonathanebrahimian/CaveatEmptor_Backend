from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId
from app.models.classes import LabsSchema
import uuid
from enum import Enum

class Status(str, Enum):
    OPEN = "OPEN"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"

class LabAppSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    status: Status = Status.OPEN
    lab_id: str
    class_id: str


class ApplicationSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: EmailStr
    name: str
    time: datetime
    resume: str
    labs: list[LabAppSchema]
    

    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@mail.com",
                "name": "John Doe",
                "time": "2021-09-01T00:00:00",
                "resume": "resume.pdf",
                "labs":[{
                    'lab_id':'',
                    'class_id':'',
                    "status": "OPEN"
                },{
                    'lab_id':'',
                    'class_id':'',
                    "status": "OPEN"
                }]
            }
        }


class UpdateApplicationModel(BaseModel):
    email: Optional[EmailStr]
    status: Optional[Status]
    name: Optional[str]
    time: Optional[datetime]
    resume: Optional[str]
    labs: Optional[list[LabsSchema]]

    class Config:
        schema_extra = {
            "labs": {
                "name": "CS 4351",
                "active":True,
                "labs":[{
                    'lab_id':'',
                    'class_id':'',
                    "status": "OPEN"
                },{
                    'lab_id':'',
                    'class_id':'',
                    "status": "OPEN"
                }]
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
