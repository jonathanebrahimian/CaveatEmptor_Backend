from fastapi import APIRouter

from app.database import report_collection,stats_collection

router = APIRouter()

@router.get("/", response_description="Get analysis")
async def algo_update():
    report_collection.delete_many({})
    stats_collection.delete_many({})
    return True



