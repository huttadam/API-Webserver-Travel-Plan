from init import db, ma
from datetime import datetime
from marshmallow import fields
from marshmallow.validate import Regexp


class Activity(db.Model):
    __tablename__ = "activities"
    #Primary Key
    id = db.Column(db.Integer, primary_key=True)

    #Table Feilds
    activity_name = db.Column(db.String(100), nullable=False, unique = True)
    activity_location_URL = db.Column(db.String)
    budget = db.Column(db.Integer)
    date_available = db.Column(db.String(50), default= 'Anytime')
    activity_desc = db.Column(db.String(150), nullable=False)

    # Foreign Key
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    
    #Relationships
    destination = db.relationship('Destination', back_populates='activities')
    comments = db.relationship('Comment', back_populates='activity', cascade= 'all, delete')
 

class ActivitySchema(ma.Schema):
    activity_location_URL = fields.Str(validate=Regexp("^https://maps\.app\.goo\.gl/[-a-zA-Z0-9@:%._+~#=]{1,256}$", error="Invalid URL format, please only use Google Maps, Short URL"))
    comments = fields.Nested('CommentSchema', many= True, exclude= ['id'])

    # validates the URL input to make sure its shortened and only from google maps (Trusted source)

    class Meta:
        fields = ("id","activity_name", "activity_location_URL", "budget", "activity_desc","date_available", "comments","destination_id")