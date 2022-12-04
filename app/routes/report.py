from fastapi import APIRouter

from app.database import report_collection,stats_collection
import requests
import json
from datetime import datetime

router = APIRouter()

LAMBDA_ROUTE = "https://cum5mb2rwyem2eip5dc6lxqz5m0moipt.lambda-url.us-east-2.on.aws/"


@router.get("/", response_description="Get analysis")
async def get_analysis(token: str):
    db_report = report_collection.find_one({'address':token})
    if db_report is not None:
        print("cached")
        report = db_report['report']
    else:
        print("not cached")
        report = call_lambda(token)
        if not report:
            return {'message':"Error producing report",'status':500}
    
    report = json.loads(report)
    query_stats(report)
    return {
        'report':report,
        'status':200
    }


def call_lambda(token):
    params = {
        'token':token
    }
    response = requests.get(LAMBDA_ROUTE,params=params)
    if 200 <= response.status_code <= 201:
        report = response.json()
        store_stats(report)
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

def store_stats(report):
    for contract in report['contracts']:
        if not contract['main']:
            stats_collection.update_one({'contract':contract['name']},{'$inc':{'count':1}},upsert=True)

def query_stats(report):
    for contract in report['contracts']:
        percent_seen = None
        if not contract['main']:
            percent_seen = stats_collection.find_one({'contract':contract['name']})['count'] / report_collection.count_documents({})
        contract['percent_seen'] = percent_seen

