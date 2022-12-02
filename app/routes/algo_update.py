from fastapi import APIRouter

from app.database import algo_update_collection,report_collection,database
import requests
import json
from datetime import datetime

router = APIRouter()



@router.get("/", response_description="Get analysis")
async def algo_update():
    report_collection.delete_many({})
    return True



