from init import db, ma



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique = True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    admin_acc = db.Column(db.Boolean, default=False)

    trips = db.relationship('Trip', back_populates='user', cascade= 'all, delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "admin_acc", "f_name", "l_name")