from fastapi import APIRouter
from app.core.security import create_access_token
from app.core.security import verify_access_token

router = APIRouter()

@router.get("/token")
async def token():
    
    token = create_access_token(
        {
            "user_id": 1
        }
    )
    
    return token
    
# @router.get("/verify")
# async def verify():
    
#     payload = verify_access_token(token=token)
    
#     return payload