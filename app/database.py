import pymongo
import os

MONGO_DETAILS = os.environ.get('MONGODB_URI_SRV')

client = pymongo.MongoClient(MONGO_DETAILS)

database = client.caveat_emptor

report_collection = database.get_collection("report")
report_collection.create_index([("address", pymongo.ASCENDING)], unique=True)

stats_collection = database.get_collection("stats")
algo_update_collection = database.get_collection("algo_update")

