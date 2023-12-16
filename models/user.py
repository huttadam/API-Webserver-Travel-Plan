from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp, And, Length



class User(db.Model):
    __tablename__ = 'users'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    #Table Feilds
    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique = True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    admin_acc = db.Column(db.Boolean, default=False)

    #Relationships
    trips = db.relationship('Trip', back_populates='user', cascade= 'delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')


# User information serialized via Marshamallow
class UserSchema(ma.Schema):
    #validating some feilds and checking user input prior to insertion into DB/Schema
    f_name = fields.String(validate=And(Length(min=1, error='Please enter at least one character.'), Regexp('^[a-zA-Z ]+$', error='Please enter letters only.')))
    l_name = fields.String(validate=And(Length(min=1, error='Please enter at least one character.'), Regexp('^[a-zA-Z ]+$', error='Please enter letters only.')))
    username = fields.String(validate= Regexp('^[a-zA-Z0-9_]{3,20}$', error = "Invalid username, Must be at least 3 Chars"))
    password = fields.String(validate= Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z\d@$#$^()!%*?&]{10,}$', error='Password must have a minimum of ten characters + At least one uppercase letter, lowercase letter and number'))
    email = fields.String(validate= Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', error = "Invalid Email address, please check and re-enter"))

    #f_name and l_name must be longer than 1 and contain only alphabetic characters
    # username must be a certain length
    # password must be a 10 char min and contain at least one uppercase letter, lowercase letter and number
    # email must conform to standard formatting (letters or numbers- can contain . or _ have an @ and the followed by the domain. )


    class Meta:
        fields = ("id", "username", "email", "password", "admin_acc", "f_name", "l_name")
