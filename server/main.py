from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from . import models
from .db import engine, SessionLocal 
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class CourseBase(BaseModel):
    title : str
    discriptation : str
    duration : str
   

class UserBase(BaseModel):

    username: str

class VideoBase(BaseModel):
     
    title : str 
    url : str

class QuizBase(BaseModel):
    
    title : str 
    question : str
    answer : str

def get_db():

    db = SessionLocal() 

    try:

        yield db

    finally:

        db.close()

db_dependency = Annotated [Session, Depends(get_db)]

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/users/", status_code=201)
async def create_user(user: UserBase, db: Session = Depends(get_db)):

    # Assuming db_dependency is a SQLAlchemy Session
    query = text(
        f"INSERT INTO users (username) "
        f"VALUES ('{user.username}')"
    )

    try:
        db.execute(query)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    return {"message": "User created successfully"}


from sqlalchemy import select

# ... (previous imports and code)

# Get a user by ID
from fastapi import HTTPException

@app.get("/users/{user_id}", response_model=UserBase)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    query = text(f"SELECT * FROM users WHERE id = {user_id}")
    user = db.execute(query).fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserBase(id=user[0], username=user[1])  # Adjust the column indices based on your actual schema


# Delete a user by ID
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    query = text(f"DELETE FROM users WHERE id = {user_id}")
    try:
        result = db.execute(query)
        db.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    return {"message": "User deleted successfully"}


# get all courses
# @app.get("/course/get")
# def read_courses(db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM courses").fetchall()
#     return result

# # get course by id
# @app.get("/course/{course_id}/get")
# def read_course(course_id: int, db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM courses WHERE id = :course_id", {"course_id": course_id}).fetchone()
#     return result

# # get all videos
# @app.get("/video/get")
# def read_videos(db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM videos").fetchall()
#     return result

# # add video
# @app.post("/video/create")
# def create_video(title: str, course_id: int, db: Session = Depends(get_db)):
#     db.execute(text(f"INSERT INTO videos (title, course_id) VALUES ({title}, {course_id})"))
#     db.commit()

# # get video by id
# @app.get("/video/{video_id}/get")
# def read_video(video_id: int, db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM videos WHERE id = :video_id", {"video_id": video_id}).fetchone()
#     return result

# # get all quizzes
# @app.get("/quiz/get")
# def read_quizzes(db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM quizzes").fetchall()
#     return result

# # add quiz
# @app.post("/quiz/create")
# def create_quiz(questions: str, course_id: int, db: Session = Depends(get_db)):
#     db.execute(text(f"INSERT INTO quizzes (questions, course_id) VALUES ({questions}, {course_id})"))
#     db.commit()

# # get quiz by id
# #@app.get("/quiz/{quiz_id}/get")
# #def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
#     result = db.execute("SELECT * FROM quizzes WHERE id = :quiz_id", {"quiz_id": quiz_id}).fetchone()
#     return result