from fastapi import FastAPI

from app.routes.report import router as AnalyzeRouter

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AnalyzeRouter, tags=["Analyze"], prefix="/analyze")


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