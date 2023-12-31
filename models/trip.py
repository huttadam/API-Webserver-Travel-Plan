from init import db, ma
from datetime import datetime, timedelta
from marshmallow import fields
from marshmallow.validate import Regexp


class Trip(db.Model):
    __tablename__ = 'trips'
    #Primary Key
    id = db.Column(db.Integer, primary_key=True)
    #Table Feilds
    trip_name = db.Column(db.String(70), nullable=False, unique = True)
    start_date = db.Column(db.Date, nullable=False)
    finish_date = db.Column(db.Date, nullable=False)
    estimated_budget = db.Column(db.Integer, nullable=False)
    trip_desc = db.Column(db.Text, nullable=False)

    #Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    #Relationships
    user = db.relationship('User', back_populates='trips')
    destinations = db.relationship('Destination', back_populates='trip', cascade='all, delete')

# This Schema shows destination information with some exclusions
class TripSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username'])
    destinations = fields.Nested('DestinationSchema', exclude=['activities'], many= True)

    class Meta:
        fields = ("id", "trip_name","start_date", "finish_date",'estimated_budget',"trip_desc","user", "destinations")


# This Schema is used to show addtional destination information without user info
class FullTripSchema(ma.Schema):
    destinations = fields.Nested('DestinationSchema', many= True, exclude=['activities.activity_location_URL', 'continent'])

    class Meta:
        fields = ("id", "trip_name","start_date", "finish_date",'estimated_budget',"trip_desc", "destinations")

