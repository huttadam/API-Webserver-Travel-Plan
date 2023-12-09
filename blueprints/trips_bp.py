from models.trip import Trip, TripSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize

bp_trips = Blueprint("bp_trips",__name__, url_prefix='/trips')

#All  Users Trips --- Admin Only
@bp_trips.route('/')
@jwt_required()
def read_all_trips():
    # NEED TO ADD ADMIN ONLY HERE
    stmt = db.select(Trip)
    trips = db.session.scalars(stmt).all()
    return TripSchema(many=True).dump(trips)


# Users read there own personal trips - Individually - NEED TO ADD OWNER TO VIEW
@bp_trips.route('/<int:id>')
@jwt_required()
def read_single_trip(id):
    stmt = db.select(Trip).filter_by(id=id)
    trip = db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.id)
        return TripSchema().dump(trip)
    else:
        return {'error': 'Card not found'}, 404

#Create a Trip
@bp_trips.route('/', methods=['POST'])
@jwt_required()
def create_trip():
    
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

# Update a trip
@bp_trips.route('/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_trip(id):
    trip_info = TripSchema(exclude=['id']).load(request.json)
    stmt = db.select(Trip).filter_by(id=id)
    trip = db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.id)
        trip.trip_name = trip_info.get('trip_name', trip.trip_name),
        trip.start_date = trip_info.get('start_date', trip.start_date),
        trip.finish_date = trip_info.get('finish_date',trip.finish_date),
        trip.estimated_budget = trip_info.get('estimated_budget', trip.estimated_budget),
        trip.trip_desc = trip_info.get('trip_desc', trip.trip_desc)

        db.session.commit()

        return TripSchema().dump(trip)
   
    else:
        return {'Error': 'Trip not found'}, 404

#Delete a trip
@bp_trips.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_trip(id):
    stmt =db.select(Trip).filter_by(id = id)
    trip =db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.id)
        db.session.delete(trip)
        db.session.commit()
        return {'Success': f'Trip ID: {id} and all related content deleted'}