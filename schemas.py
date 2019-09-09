from marshmallow_sqlalchemy import ModelSchema
from models import Home

from marshmallow import Schema, fields, pprint

# class HomeSchema(ModelSchema):
#     class Meta:
#         model = Home

class HomeSchema(ModelSchema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        fields = ("id", "sell", "list", "living", "rooms", "beds", "baths", "age", "acres", "taxes")
        ordered = True