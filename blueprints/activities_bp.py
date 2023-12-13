from models.activity import Activity, ActivitySchema
from models.destination import Destination, DestinationPublicSchema
from models.trip import Trip, TripSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize, admin_only


bp_activities = Blueprint("bp_activities",__name__, url_prefix='/activities')

#All  Users activities - Admin only
@bp_activities.route('/A')
@jwt_required()
def read_all_activities():
    admin_only()
    stmt = db.select(Activity)
    activities = db.session.scalars(stmt).all()
    return ActivitySchema(many=True, exclude= ['comments']).dump(activities)

@bp_activities.route('/<int:activity_id>')
@jwt_required()
def read_single_activity(activity_id):
    stmt = db.select(Activity).filter_by(id=activity_id)
    activity = db.session.scalar(stmt)
    if activity:
        owner_admin_authorize(activity.destination.trip.user.id)
        return ActivitySchema(exclude=['comments']).dump(activity)
    else:
        return {'Error': 'Activity_ID not found'}, 404


#Create a activity
@bp_activities.route('/', methods=['POST'])
@jwt_required()
def create_activity():
    activity_info = ActivitySchema().load(request.json)

    user_id = get_jwt_identity()
    
    # Ensure that the user is the owner of the Destination associated with the Activity
    dest_id = activity_info.get('destination_id')
    dest = Destination.query.get(dest_id)
    
    if not dest or dest.trip.user_id != user_id:
        return {'Error': 'Invalid destination ID or unauthorized access'}, 401
    else:
        activity = Activity(
            activity_name=activity_info.get('activity_name'),
            activity_location_URL=activity_info.get('activity_location_URL'),
            budget=activity_info.get('budget'),
            date_available=activity_info.get('date_available'),
            activity_desc=activity_info.get('activity_desc'),
            destination_id=dest_id
        )

        db.session.add(activity)
        db.session.commit()

        return ActivitySchema().dump(activity), 201

# Update a activity
@bp_activities.route('/<int:activity_id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_activity(activity_id):
    act_info = ActivitySchema(exclude=['id']).load(request.json)
    stmt = db.select(Activity).filter_by(id=activity_id)
    act = db.session.scalar(stmt)
    if act:
        owner_admin_authorize(act.destination.trip.user.id)
        act.activity_name = act_info.get('activity_name', act.activity_name),
        act.activity_location_URL = act_info.get('activity_location_URL', act.activity_location_URL),
        act.budget = act_info.get('budget',act.budget),
        act.date_available= act_info.get('date_available', act.date_available),
        act.activity_desc = act_info.get('activity_desc', act.activity_desc)
        act.destination_id = act_info.get('destination_id', act.destination_id)

        db.session.commit()

        return ActivitySchema(exclude= ['comments']).dump(act)
   
    else:
        return {'Error': 'Activity not found'}, 404

#Delete a activity
@bp_activities.route('/<int:activity_id>', methods=['DELETE'])
@jwt_required()
def delete_activity(activity_id):
    stmt= db.select(Activity).filter_by(id = activity_id)
    activity= db.session.scalar(stmt)
    if activity:
        owner_admin_authorize(activity.destination.trip.user.id)
        db.session.delete(activity)
        db.session.commit()
        return {'Success': f'Activity ID: {id} and all related Comments deleted'}



@bp_activities.route('/public')
def public_activities_all():
    stmt = db.select(Destination)
    destinations = db.session.scalars(stmt).all()
    if destinations:
        return DestinationPublicSchema(many=True).dump(destinations)
    else:
        return {'Error': 'Files not found'}, 404

@bp_activities.route('/public/<int:activity_id>')
def public_activities_single_id(activity_id):
    activity = db.session.query(Activity).filter(Activity.id == activity_id).one()
    if activity:
        return ActivitySchema().dump(activity)
    else:
        return {'Error': 'Actvity_ID not found'}, 404


@bp_activities.route('/public/country/<string:dest_country>')
def public_activities_destination(dest_country):
    stmt = db.session.query(Destination).filter(Destination.dest_country == dest_country)
    destinations = stmt.all()
    if destinations:
        return DestinationPublicSchema(many=True).dump(destinations)
    else:
        return {'Error': 'Country not found'}, 404


@bp_activities.route('/public/continent/<string:continent>')
def public_activities_continent(continent):
    stmt = db.session.query(Destination).filter(Destination.continent == continent)
    destinations =stmt.all()
    if destinations:
        return DestinationPublicSchema(many=True).dump(destinations)
    else:
        return {'Error': 'Continent not found'}, 404



