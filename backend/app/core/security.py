from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.core.settings import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

# generating token here
def create_access_token(data: dict):
    
    payload = data.copy()
    
    expire = datetime.utcnow() + timedelta(hours=1)
    
    payload.update({"exp":expire})
    
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# verifying token here 
def verify_access_token(token: str):
    
    try:
        
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )
        
        return payload
        
    except JWTError:
        return None