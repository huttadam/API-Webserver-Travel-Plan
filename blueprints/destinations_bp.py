from models.destination import Destination, DestinationSchema
from flask_jwt_extended import jwt_required
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize, admin_only

bp_destinations = Blueprint("bp_destinations",__name__, url_prefix='/destinations')

#Admin Can Check All destinations
@bp_destinations.route('/A')
@jwt_required()
def read_all_destinations():
    admin_only()
    stmt = db.select(Destination)
    destinations = db.session.scalars(stmt).all()
    return DestinationSchema(many=True, exclude = ['activities']).dump(destinations)

# User can check there destinations and receive Activity information for each destination
@bp_destinations.route('/<int:dest_id>')
@jwt_required()
def read_one_destination(dest_id):
    stmt = db.select(Destination).filter_by(id = dest_id)
    dest = db.session.scalar(stmt)
    if dest:
        owner_admin_authorize(dest.trip.user.id)
        return DestinationSchema().dump(dest)
    else:
        return {'Error': 'Destination not found'}, 404


# User can add destinations to trip
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


#User can edit a destination
@bp_destinations.route('/<int:dest_id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_destination(dest_id):
    dest_info = DestinationSchema(exclude=['id']).load(request.json)
    stmt = db.select(Destination).filter_by(id=dest_id)
    dest = db.session.scalar(stmt)
    if dest:
        owner_admin_authorize(dest.trip.user.id)
        dest.dest_name = dest_info.get('dest_name', dest.dest_name)
        dest.dest_country = dest_info.get('dest_country', dest.dest_country)

        db.session.commit()

        return DestinationSchema().dump(dest)
   
    else:
        return {'Error': 'Destination not found'}, 404

#Delete a destination
@bp_destinations.route('/<int:dest_id>', methods=['DELETE'])
@jwt_required()
def delete_destination(dest_id):
    stmt= db.select(Destination).filter_by(id = dest_id)
    dest= db.session.scalar(stmt)
    if dest:
        owner_admin_authorize(dest.trip.user.id)
        db.session.delete(dest)
        db.session.commit()
        return {'Success': f'Destination ID: {id} and all related Activities deleted'},201