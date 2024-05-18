from pymongo import MongoClient
from dotenv import load_dotenv
import os

# pip install python-dotenv

load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

#! Created dummy database in mongoDB
database = client.property_management
property_collection = database.get_collection("properties")
