from tortoise.models import Model
from tortoise import fields
import secrets
from src.datalayer.models.base import ModelBase

def generate_token():
    return secrets.token_urlsafe(20)

class UserModel(ModelBase):
    name = fields.CharField(max_length=120)
    email = fields.CharField(max_length=120, unique = True)
    password = fields.TextField()
    token = fields.TextField(default = generate_token)
