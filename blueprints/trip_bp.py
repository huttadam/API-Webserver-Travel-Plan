from models.trip import Trip, TripSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, Blueprint
from init import db

bp_trips = Blueprint("bp_trips",__name__, url_prefix='/trips')

#Users read there own personal Trips
@bp_trips.route('/')
@jwt_required()
def mytrips():
    current_user_id = get_jwt_identity()
    stmt = db.select(Trip).where(Trip.user_id == current_user_id)
    trips = db.session.scalars(stmt).all()
    return TripSchema(many=True).dump(trips)

#Create a Trip
@bp_trips.route('/', methods=['POST'])
@jwt_required()
def create_trips():
    trip_info = TripSchema().load(request.json)
    
    trip = Trip(
        trip_name = trip_info.get('trip_name'),
        start_date = trip_info.get('start_date'),
        finish_date = trip_info.get('finish_date'),
        estimated_budget = trip_info.get('estimated_budget'),
        trip_desc = trip_info.get('trip_desc'),

        user_id = get_jwt_identity()
    )

    db.session.add(trip)
    db.session.commit()

    return TripSchema().dump(trip), 201

#Edit a trip

