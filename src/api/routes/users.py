from fastapi import APIRouter, Depends
from src.api.dtos.users import UserRegistration, UserLogin
from typing import Annotated
from src.services.user import UserService

router = APIRouter(prefix="/users", tags=["users"], responses={418: {"description": "I'm a teapot"}})

@router.post("/register")
async def register(body: UserRegistration, service: Annotated[UserService, Depends(UserService)]):

    response =  await service.register(name = body.name, email = body.email, password = body. password)
    return [{"created": response}]

@router.post("/login")
async def login(body: UserLogin, service: Annotated[UserService, Depends(UserService)]):

    response = await service.login(email = body.email,password = body.password)
    return { "logged": response}

@router.get("/all-users")
async def get_all_users(service: Annotated[UserService, Depends(UserService)]):
    return await service.get_all_users()



