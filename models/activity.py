from init import db, ma
from datetime import datetime
from marshmallow import fields


class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)

    activity_name = db.Column(db.String, nullable=False)
    activity_location_URL = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    date_available = db.Column(db.String, default= 'Anytime')
    activity_desc = db.Column(db.String(100), nullable=False)

    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    destination = db.relationship('Destination', back_populates='activities')

    comments = db.relationship('Comment', back_populates='activity')
 

class ActivitySchema(ma.Schema):
    comments = fields.Nested('CommentSchema', many= True, exclude= ['id'])
    # destination = fields.Nested('DestinationSchema', exclude= ['id'])

    class Meta:
        fields = ("id","activity_name", "activity_location_URL", "budget", "activity_desc","date_available", "comments" )