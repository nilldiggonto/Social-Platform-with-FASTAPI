from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DB_URL = "postgresql://postgres:nill1234@localhost:5432/fastsocial"

engine = create_engine(SQLALCHEMY_DB_URL)

LocalSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()