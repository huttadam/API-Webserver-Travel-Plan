from init import db, ma
from datetime import datetime
from marshmallow import fields


class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)

    dest_country = db.Column(db.String, nullable = False)
    dest_name = db.Column(db.String, nullable = False)
    continent = db.Column(db.String, nullable = False)

    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    trip = db.relationship('Trip', back_populates='destinations')

    activities = db.relationship('Activity', back_populates='destination', cascade='all, delete')
    


class DestinationSchema(ma.Schema):
    activities = fields.Nested('ActivitySchema', many = True, exclude=['comments'])

    class Meta:
        fields = ( "id","dest_country", "dest_name","continent","activities", "trip_id")

class DestinationPublicSchema(ma.Schema):
    activities = fields.Nested('ActivitySchema', many = True, exclude=['budget'])

    class Meta:
        fields = ( "id","dest_country", "dest_name", "activities", "continent")






