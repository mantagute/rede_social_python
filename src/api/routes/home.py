from fastapi import APIRouter
from src.datalayer.models.user import UserModel
from typing import Annotated
from fastapi import Depends
from src.api.authentication import verify_token
router = APIRouter(prefix="/me", tags=["me"], responses={404: {"description": "I'm a teapot"}})

# meu token: "Y_3AJ-B81S-n91V25aKY4sRqLZY"
@router.post("/")
async def my_informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    print("current_user", current_user)
    return {"result": f"Ola, {current_user.name}"}

