from init import db, ma


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message= db.Column(db.String)

    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship('Activity', back_populates='comments')

 
class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id","message", "activity_id")