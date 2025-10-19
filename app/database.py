import time
from typing import Annotated
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from psycopg2.extras import RealDictCursor
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine= create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:

  #try:
      #conn= psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='080202', cursor_factory=RealDictCursor)
      #cursor= conn.cursor()
      #print('Database Connection was Successful')
      #break
  
  #except Exception as error:
      #print("connecting to the database failed")
      #print("Error:",error)
      #time.sleep(2)
