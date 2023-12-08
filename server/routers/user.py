from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user():
    pass

@router.get("/get", status_code=status.HTTP_200_OK)
def get_user():
    pass