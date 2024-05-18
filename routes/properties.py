from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from config.db import property_collection
from models.Property import Property, PropertyResponse
from schema.property_helper import property_helper

property_router = APIRouter()

@property_router.get(
    "/",
)
async def read_root():
    return {"greetings": "Welcome to Property Management System!"}

#! Create a new property
@property_router.post("/properties", response_model=List[PropertyResponse])
async def create_new_property(property: Property):
    result = property_collection.insert_one(property.dict())
    properties = property_collection.find()
    return [property_helper(prop) for prop in properties]

#! Fetch property details by city
@property_router.get("/properties/city/{city_name}", response_model=List[PropertyResponse])
async def fetch_property_details(city_name: str):
    properties = property_collection.find({"city": city_name})
    return [property_helper(prop) for prop in properties]

#! Update property details by using put as to update only changed details
@property_router.put("/properties/{property_id}", response_model=List[PropertyResponse])
async def update_property_details(property_id: str, property: Property):
    if not ObjectId.is_valid(property_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid property ID")
    
    updated_property = property_collection.find_one_and_update(
        {"_id": ObjectId(property_id)},
        {"$set": property.dict()},
        return_document=True
    )

    if not updated_property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")

    properties = property_collection.find()
    return [property_helper(prop) for prop in properties]

#! Find cities by state
@property_router.get("/properties/state/{state_name}", response_model=List[str])
async def find_cities_by_state(state_name: str):
    cities = property_collection.distinct("city", {"state": state_name})
    return cities

#! Find similar properties by property ID
@property_router.get("/properties/similar/{property_id}", response_model=List[PropertyResponse])
async def find_similar_properties(property_id: str):
    if not ObjectId.is_valid(property_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid property ID")

    property = property_collection.find_one({"_id": ObjectId(property_id)})
    if not property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
    same_city = property_collection.find({"city": property["city"]}) #! list of same cities in the database as the one whose property id is given
    return [property_helper(prop) for prop in same_city]
