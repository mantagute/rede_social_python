from pydantic import BaseModel

class PostCreation(BaseModel):
    message: str