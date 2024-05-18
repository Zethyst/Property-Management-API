from fastapi import FastAPI
from routes.properties import property_router

app = FastAPI()

app.include_router(property_router, prefix="/api")

if __name__ == "__index__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#! Run the application using uvicorn app.index:app --reload
