from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:ojasman%40%231109@localhost:5432/telusko"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush=False, bind = engine)