from init import db, ma


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message =db.Column(db.String)

 
class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id","comment")