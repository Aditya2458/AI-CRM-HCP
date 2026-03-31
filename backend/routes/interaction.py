from fastapi import APIRouter
from pydantic import BaseModel

# create router
router = APIRouter()

# request schema
class Interaction(BaseModel):
    hcp_name: str
    topics: str
    sentiment: str

# API route
@router.post("/interactions")
def create_interaction(data: Interaction):
    return {
        "message": "Interaction saved ✅",
        "data": data
    }