from fastapi import APIRouter

from app.database import report_collection,algo_update_collection
import requests
import json
from datetime import datetime

router = APIRouter()

LAMBDA_ROUTE = "https://cum5mb2rwyem2eip5dc6lxqz5m0moipt.lambda-url.us-east-2.on.aws/"


@router.get("/", response_description="Get analysis")
async def get_analysis(token: str):
    last_algo_update = algo_update_collection['latest']
    db_report = report_collection.find_one({'address':token})
    print(db_report)
    last_algo_update = None
    if db_report is not None and (last_algo_update is None or last_algo_update < db_report['timestamp']):
        print("cached")
        report = db_report['report']
    else:
        print("not cached")
        report = call_lambda(token)
        if not report:
            return {'message':"Error producing report",'status':500}
    
    report = json.loads(report)
    return {
        'report':report,
        'status':200
    }



# datetime object containing current date and time
    return ResponseModel(analysis, "Classes data retrieved successfully")


def call_lambda(token):
    params = {
        'token':token
    }
    response = requests.get(LAMBDA_ROUTE,params=params)
    print(response)
    if 200 <= response.status_code <= 201:
        report = response.json()
        str_report = json.dumps(report)
        timestamp = datetime.now()
        report_obj = {
            'address':token,
            'report':str_report,
            'timestamp':timestamp
        }
        report_collection.insert_one(report_obj)
        return str_report

    return False