from tortoise.models import Model
from tortoise import fields
import secrets
from src.datalayer.models.base import ModelBase

class PostModel(ModelBase):
    user = fields.ForeignKeyField("models.UserModel", related_name = "posts")
    message = fields.TextField()
    