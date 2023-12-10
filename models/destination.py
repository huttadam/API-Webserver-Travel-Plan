from init import db, ma
from datetime import datetime
from marshmallow import fields


class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)

    dest_country = db.Column(db.String, nullable = False)
    dest_name = db.Column(db.String, nullable = False)

    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    trip = db.relationship('Trip', back_populates='destinations')

    activities = db.relationship('Activity', back_populates='destination', cascade='all, delete')
    


class DestinationSchema(ma.Schema):
    # trips = fields.Nested('TripSchema', many = True, exclude = ['users',"destinations"])
    # activities = fields.Nested('ActivitySchema', exclude = ['id', 'budget'], many= True)

    class Meta:
        fields = ("id", "dest_country", "dest_name")
        ordered =True