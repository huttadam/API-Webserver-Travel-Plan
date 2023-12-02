from init import db, ma
from datetime import datetime, timedelta


class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)

    trip_name = db.Column(db.String(70), nullable=False, unique = True)
    start_date = db.Column(db.Date, nullable=False)
    finish_date = db.Column(db.Date)
    estimated_budget = db.Column(db.Integer, nullable=False)
    trip_desc = db.Column(db.Text, nullable=False)

class TripSchema(ma.Schema):
    class Meta:
        fields = ("id", "trip_name","start_date", "finish_date",'estimated_budget',"trip_desc",)
   