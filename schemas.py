from marshmallow_sqlalchemy import ModelSchema
from models import Home

from marshmallow import Schema, fields, pprint

class HomeSchema(ModelSchema):
    class Meta:
        model = Home