import motor.motor_asyncio
from bson.objectid import ObjectId
import json
import pymongo
from bson.json_util import dumps
from bson import json_util

MONGO_DETAILS = "mongodb://root:rootpassword@mongodb_container:27017"

client = pymongo.MongoClient(MONGO_DETAILS)

database = client.caveat_emptor

report_collection = database.get_collection("report")
