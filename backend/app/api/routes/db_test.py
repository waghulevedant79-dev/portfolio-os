from fastapi import APIRouter
from app.db.database import test_database_connection

router = APIRouter()

@router.get("/db-test")
async def db_test():
    
    test_database_connection()
    
    return {
        "message": "Database Connected Succuessfully."
    }