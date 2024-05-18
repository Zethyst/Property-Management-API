from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str
    address: str
    city: str
    state: str

class PropertyResponse(Property):
    id: str
