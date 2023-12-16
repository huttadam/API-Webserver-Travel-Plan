from init import db, ma
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = "comments"
    #Primary key
    id = db.Column(db.Integer, primary_key=True)

    #Table Fields
    message= db.Column(db.String(200), nullable=False)
    
    #Foreign Keys
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    
    #Relationships
    activity = db.relationship('Activity', back_populates='comments', cascade='all, delete')
    user = db.relationship('User', back_populates='comments')

 
class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ['username'])

    class Meta:
        fields = ("id","message","user","activity_id")