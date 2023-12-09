from init import db, ma
from marshmallow import fields


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message= db.Column(db.String)

    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship('Activity', back_populates='comments')

    user_username = db.Column(db.String, db.ForeignKey('users.username'))
    user = db.relationship('User', back_populates='comments')

 
class CommentSchema(ma.Schema):
    # users = fields.Nested('UserSchema', only = ['username'])

    class Meta:
        fields = ("id","message")