from fastapi import FastAPI

from app.routes.report import router as AnalyzeRouter
from app.routes.algo_update import router as AlgoUpdateRouter
from enum import Enum
import os

from fastapi.middleware.cors import CORSMiddleware

class Env(Enum):
    LOCAL = "LOCAL"
    PROD = "PROD"

    def deployed(self):
        if self in [Env.PROD]:
            return True
        else:
            return False

ENV = Env(os.environ.get("ENV"))

if ENV.deployed():
    allow_origins = ['']
    allow_methods = ['']
    allow_headers = ['']
else:
    allow_origins = ['*']
    allow_methods = ['*']
    allow_headers = ['*']

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=allow_origins,
	allow_credentials=True,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(AnalyzeRouter, tags=["Analyze"], prefix="/analyze")
app.include_router(AlgoUpdateRouter, tags=["Algo Update"], prefix="/algoupdate")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.on_event("startup")
def startup_db_client():
    # app.mongodb_client = MongoClient("mongodb://root:rootpassword@mongodb_container:27017")
    # app.database = app.mongodb_client["SourceTA"]
    # app.database['users'].create_index([("email", pymongo.ASCENDING)], unique=True)
    pass

@app.on_event("shutdown")
def shutdown_db_client():
    # app.mongodb_client.close()
    pass