from init import db, ma
from datetime import datetime


class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)

    activity_name = db.Column(db.String, nullable=False)
    activity_location_URL = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    date_available = db.Column(db.String, default= 'Anytime')
    activity_desc = db.Column(db.String(100), nullable=False)

 

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ("id","activity_name", "activity_location_URL", "budget","activity_desc")