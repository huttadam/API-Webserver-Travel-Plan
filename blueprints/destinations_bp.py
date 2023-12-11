from models.destination import Destination, DestinationSchema
from flask_jwt_extended import jwt_required
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize, admin_only

bp_destinations = Blueprint("bp_destinations",__name__, url_prefix='/destinations')

#Admin Can Check All destinations
@bp_destinations.route('/All')
@jwt_required()
def read_all_destination():
    admin_only()
    stmt = db.select(Destination)
    destinations = db.session.scalars(stmt).all()
    return DestinationSchema(many=True).dump(destinations)

@bp_destinations.route('/<int:trip_id>')
@jwt_required()
def read_users_destinations(trip_id):
    owner_admin_authorize(trip_id)
    stmt = db.select(Destination).filter_by(trip_id=trip_id)
    dests = db.session.scalars(stmt)
    if dests:
        return DestinationSchema(many = True).dump(dests)
    else:
        return {'Error': 'Destination not found'}, 404



@bp_destinations.route('/', methods=['POST'])
@jwt_required()
def create_destination():
    dest_info = DestinationSchema(exclude=['id']).load(request.json)
    
    destination = Destination(
        dest_name = dest_info.get('dest_name'),
        dest_country = dest_info.get('dest_country'),
        trip_id = dest_info.get('trip_id')
    )

    db.session.add(destination)
    db.session.commit()

    return DestinationSchema().dump(destination), 201



@bp_destinations.route('/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_destination(trip_id):
    dest_info = DestinationSchema(exclude=['id']).load(request.json)
    stmt = db.select(Destination).filter_by(id=trip_id)
    dest = db.session.scalar(stmt)
    if dest:
        owner_admin_authorize(dest.trip.id)
        dest.dest_name = dest_info.get('dest_name', dest.dest_name)
        dest.dest_country = dest_info.get('dest_country', dest.dest_country)

        db.session.commit()

        return DestinationSchema().dump(dest)
   
    else:
        return {'Error': 'Destination not found'}, 404

#Delete a destination
@bp_destinations.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_destination(id):
    stmt= db.select(Destination).filter_by(id = id)
    dest= db.session.scalar(stmt)
    if dest:
        owner_admin_authorize(dest.id)
        db.session.delete(dest)
        db.session.commit()
        return {'Success': f'Destination ID: {id} and all related Activities deleted'}