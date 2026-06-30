from fastapi import APIRouter
from app.core.security import verify_access_token
from app.api.routes.token import token
# from app.core.security import create_access_token

router = APIRouter()

@router.get("/verify")
async def verify():

    
    payload = verify_access_token(token)
    
    return payload
