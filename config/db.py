from pymongo import MongoClient

MONGO_URI = "mongodb+srv://zethyst:akshat2002@cluster0.wdelwkx.mongodb.net"
client = MongoClient(MONGO_URI)

#! Created dummy database in mongoDB
database = client.property_management
property_collection = database.get_collection("properties")
