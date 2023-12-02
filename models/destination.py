from init import db, ma
from datetime import datetime


class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)

    dest_country = db.Column(db.String, nullable = False)
    dest_name = db.Column(db.String, nullable = False)
 

class DestinationSchema(ma.Schema):
    class Meta:
        fields = ("id", "dest_country", "dest_name")