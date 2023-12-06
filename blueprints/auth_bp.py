from flask import Blueprint, request
from models.user import User, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta


bp_users = Blueprint("bp_users",__name__, url_prefix='/users')

# Admin Searches all users (NEED JWT)
@bp_users.route('/all')
def get_all():
    # Add admin Reqd 
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()

    return UserSchema(many = True, exclude = ['password']).dump(users)

# Admin Searches for specific user ---(NEEDS AUTHORIZING-ADMIN ONLY ) + JWT
@bp_users.route('/<int:user_id>')
def get_single_user(user_id):
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if user:
        #Add Admin Reqd here
        return UserSchema(exclude = ['password']).dump(user)
    else:
        return {'Error': f'User ID {user_id} not found'}


@bp_users.route('/<int:user_id>', methods = ['DELETE'])
def admin_delete_user(user_id):
    stmt =db.select(User).filter_by(id = user_id)
    user =db.session.scalar(stmt)

    if user:
        # Add Admin Reqd HERE
        db.session.delete(user)
        db.session.commit()
        return {'Success': f'User ID {user_id} and all related content deleted'}



# User Creates Acc --NO AUTH
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


# User Log in - NO AUTH -- NEED
@bp_users.route('/login', methods=['POST'])
def login():
    try:
        user_info = UserSchema(exclude=['id', 'f_name', 'l_name', 'admin_acc','username']).load(request.json)
        user = User.query.filter_by(email=user_info['email']).first()

        if user and bcrypt.check_password_hash(user.password, user_info['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(hours = 4))
            
            return {
                'user': UserSchema(exclude=['password', 'admin_acc', 'id']).dump(user),
                'token': token
                }
        else:
            return { 'Error': 'Incorrect email address or password , Please try again'},401

    except KeyError:
        return {"Error": "Email and Password need to be provided."},400

