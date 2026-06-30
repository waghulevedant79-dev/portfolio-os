from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from app.core.settings import settings


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def test_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


def get_db():
    
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()