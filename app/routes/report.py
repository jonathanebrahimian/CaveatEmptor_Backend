from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends



from app.models.classes import (
    ResponseModel,
)

from app.database import class_collection

router = APIRouter()



@router.get("/", response_description="Get analysis")
async def get_analysis(token: str):
    analysis = token
    
    return ResponseModel(analysis, "Classes data retrieved successfully")
