from sqlalchemy import Boolean, Column, Integer, String 
from .db import Base

class User(Base):

    __tablename__ = 'users'

    id = Column (Integer, primary_key=True, index=True) 
    username = Column (String(50), unique=True)
    password = Column (String(50))
    email = Column (String(50), unique=True)

class Course(Base):
    __tablename__ = 'courses'

    id = Column (Integer, primary_key=True, index=True) 
    title = Column (String(50))
    discriptation = Column (String(50))
    duration = Column (String(50))

class video(Base):
    __tablename__ = 'video'
    id = Column (Integer, primary_key=True, index=True) 
    title = Column (Integer, index=True) 
    url = Column (String(50))

class quiz(Base):
    __tablename__ = 'quiz'

    id = Column (Integer, primary_key=True, index=True) 
    title = Column (String(50))
    question = Column (String(50))
    answer = Column (String(50))
   

