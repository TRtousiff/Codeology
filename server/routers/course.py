from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body

router = APIRouter(
    prefix="/course",
    tags=['course']
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_course():
    pass
@router.get("/get", status_code=status.HTTP_200_OK)
def get_course():
    return ["course 1", "course 2"]
