from models.activity import Activity, ActivitySchema
from flask_jwt_extended import jwt_required
from flask import request, Blueprint
from init import db


bp_activities = Blueprint("bp_activities",__name__, url_prefix='/activities')

#All  Users activities --- NEED TO ADD OWNER TO VIEW
@bp_activities.route('/')
@jwt_required()
def read_all_activities():
    stmt = db.select(Activity)
    activities = db.session.scalars(stmt).all()
    return ActivitySchema(many=True).dump(activities)


# Users read there own personal activities - Individually - NEED TO ADD OWNER TO VIEW
@bp_activities.route('/<int:id>')
@jwt_required()
def read_single_activity(id):
    stmt = db.select(Activity).filter_by(id=id)
    activity = db.session.scalar(stmt)
    if activity:
        return ActivitySchema().dump(activity)
    else:
        return {'error': 'Card not found'}, 404

#Create a activity
@bp_activities.route('/', methods=['POST'])
@jwt_required()
def create_activity():
    activity_info = ActivitySchema().load(request.json)
    
    activity = Activity(
        activity_name = activity_info.get('activity_name'),
        activity_location_URL = activity_info.get('activity_location_URL'),
        budget = activity_info.get('budget'),
        date_available = activity_info.get('date_available'),
        activity_desc = activity_info.get('activity_desc')

        # user_id = get_jwt_identity()
    )

    db.session.add(activity)
    db.session.commit()

    return ActivitySchema().dump(activity), 201

# Update a activity
@bp_activities.route('/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_activity(id):
    act_info = ActivitySchema(exclude=['id']).load(request.json)
    stmt = db.select(Activity).filter_by(id=id)
    act = db.session.scalar(stmt)
    if act:
        act.activity_name = act_info.get('activity_name', act.activity_name),
        act.activity_location_URL = act_info.get('activity_location_URL', act.activity_location_URL),
        act.budget = act_info.get('budget',act.budget),
        act.date_available= act_info.get('date_available', act.date_available),
        act.activity_desc = act_info.get('activity_desc', act.activity_desc)

        db.session.commit()

        return ActivitySchema().dump(act)
   
    # else:
    #     return {'Error': 'Activity not found'}, 404

#Delete a activity
@bp_activities.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_activity(id):
    stmt= db.select(Activity).filter_by(id = id)
    activity= db.session.scalar(stmt)
    if activity:
        db.session.delete(activity)
        db.session.commit()
        return {'Success': f'activity ID: {id} and all related content deleted'}



