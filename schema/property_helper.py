from models.Property import PropertyResponse

def property_helper(property: dict) -> PropertyResponse:
    return PropertyResponse(
        id=str(property["_id"]),
        name=property["name"],
        address=property["address"],
        city=property["city"],
        state=property["state"]
    )
