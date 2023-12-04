from flask import Blueprint, request
from models.user import User, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta


bp_users = Blueprint("bp_users",__name__, url_prefix='/users')

@bp_users.route('/register', methods=['POST'])
def register_user():

    user_info = UserSchema().load(request.json)

    double_email = db.session.query(User.email).filter_by(email=user_info["email"]).scalar()
    double_username = db.session.query(User.username).filter_by(username=user_info["username"]).scalar()
    
    if (double_email) and not  (double_email and double_username):
        return {"Error": " This Email address is already registered"}, 409

    elif (double_username) and not (double_email and double_username):
        return {"Error": "Someone already has this Username, Please change"}, 409
    
    elif (double_email) and (double_username):
        return {"Error": "Both Username and Email already registered"}, 409
    
    else:
        new_user = User (
                email=user_info['email'],
                username = user_info['username'],
                password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
                f_name=user_info['f_name'],
                l_name=user_info['l_name']
            )

        db.session.add(new_user)
        db.session.commit()

        return UserSchema(exclude=['password']).dump(new_user),201

@bp_users.route('/login')
def login():
    try:
        user_info = db.session.query(User.email == user_info['email'])
        stmt = db.session.scalar(stmt)

        if user and bcrypt.verify_password(user.password, user_info['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(hours = 4))
            
            return {
                'token': token,
                'user': UserSchema(exclude=['password']).dump(user),
                }
                
    except KeyError:
        return {"error": "Check what was entered"}

