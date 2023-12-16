from models.trip import Trip, TripSchema, FullTripSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize, admin_only

#Defines prefix for all URLs in the trips blueprint
bp_trips = Blueprint("bp_trips",__name__, url_prefix='/trips')

#All  Users Trips --- Admin Only
@bp_trips.route('/A')
@jwt_required()
def read_all_trips_admin():
    admin_only()
    stmt = db.select(Trip)
    trips = db.session.scalars(stmt).all()
    return TripSchema(many=True).dump(trips)

# Users can read all there Trips they've made (so can Admin) - Sometimes multiple in a list
@bp_trips.route('/<int:user_id>')
@jwt_required()
def read_all_users_trips(user_id):
    owner_admin_authorize(user_id)
    stmt = db.select(Trip).filter_by(user_id = user_id)
    trips = db.session.scalars(stmt).all()
    return TripSchema(many= True).dump(trips)


# Users can read all there Trips they've made (so can Admin) - A more specific search on info displayed from different schema
@bp_trips.route('/<int:user_id>/<int:trip_id>')
@jwt_required()
def read_specific_trip_info(user_id, trip_id):
    owner_admin_authorize(user_id)
    stmt = db.select(Trip).filter_by(id= trip_id)
    trip = db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.user_id)
        return FullTripSchema().dump(trip)
    else:
        return {'Error': f'Trip ID {trip_id} not found'},404
        #if / else statment handles errors



#A User with a JWT token can create a trip
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
        #auto assigns the user as the owner of the trip
    )
    db.session.add(trip)
    db.session.commit()

    return TripSchema(exclude= ["destinations"]).dump(trip), 201

# A User/owner of trip / Admin can update information 
@bp_trips.route('/<int:trip_id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_trip(trip_id):
    trip_info = TripSchema(exclude=['id']).load(request.json)
    stmt = db.select(Trip).filter_by(id = trip_id)
    trip = db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.user.id)
        trip.trip_name = trip_info.get('trip_name', trip.trip_name),
        trip.start_date = trip_info.get('start_date', trip.start_date),
        trip.finish_date = trip_info.get('finish_date',trip.finish_date),
        trip.estimated_budget = trip_info.get('estimated_budget', trip.estimated_budget),
        trip.trip_desc = trip_info.get('trip_desc', trip.trip_desc)

        db.session.commit()

        return TripSchema().dump(trip)
   
    else:
        return {'Error': f'Trip {trip_id} not found'}, 404

# A User/owner of trip / Admin can delete the trip and all related destinations
@bp_trips.route('/<int:trip_id>', methods=['DELETE'])
@jwt_required()
def delete_trip(trip_id):
    stmt =db.select(Trip).filter_by(id = trip_id)
    trip =db.session.scalar(stmt)
    if trip:
        owner_admin_authorize(trip.user.id)
        db.session.delete(trip)
        db.session.commit()
        return {'Success': f'Trip ID: {trip_id} and all related content including Destination/Activities/Comments deleted'}
    else:
        return {'Error': f'Trip {trip_id} not found'}, 404