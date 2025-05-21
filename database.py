from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DATABASE_URL = "mysql+pymysql://fastapi_user:clave123@localhost:3306/turnos_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
