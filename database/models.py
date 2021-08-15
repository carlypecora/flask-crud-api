# ~flask_api/database/models.py
from .db import db
import mongoengine_goodjson as gj

class Book(gj.Document):
    name = db.StringField(required=True, unique=True)
    characters = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
