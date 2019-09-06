from marshmallow_sqlalchemy import ModelSchema
from models import Home

class HomeSchema(ModelSchema):
    class Meta:
        model = Home