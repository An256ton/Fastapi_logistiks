from fastapi import FastAPI
from app.queries import get_forwarder_by_id
app = FastAPI()

@app.get("/get/forwarder/by/id")
async def get_get_forwarder_by_id(id):
    result= await get_forwarder_by_id(id)
    return result