from models.comment import Comment, CommentSchema
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize, admin_only

bp_comments = Blueprint("bp_comments",__name__, url_prefix='/comments')


@bp_comments.route('/A')
@jwt_required()
def read_all_comments():
    admin_only()
    stmt = db.select(Comment)
    comments = db.session.scalars(stmt).all()
    return CommentSchema(many=True).dump(comments)


@bp_comments.route('/', methods=['POST'])
@jwt_required()
def create_comments():
    comment_info = CommentSchema(exclude=['id']).load(request.json)
    
    user_id = get_jwt_identity()
    user = User.query.filter_by(id = user_id).first()

    comment = Comment(
        message = comment_info.get('message'),
        username = user.username,
        activity_id = comment_info.get('activity_id')
    )
    db.session.add(comment)
    db.session.commit()

    return CommentSchema(exclude=['activity_id']).dump(comment), 201



@bp_comments.route('/<int:comment_id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_comments(comment_id):
    comment_info = CommentSchema(exclude=['id']).load(request.json)
    stmt = db.select(Comment).filter_by(id = comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        owner_admin_authorize(comment.user.id)
        comment.message = comment_info.get('message', comment.message)

        db.session.commit()

        return CommentSchema().dump(comment)
   
    else:
        return {'Error': 'Comment not found, please check reference and try again'}, 404

#Delete a comment
@bp_comments.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comments(comment_id):
    stmt= db.select(Comment).filter_by(id = comment_id)
    comment= db.session.scalar(stmt)
    if comment:
        owner_admin_authorize(comment.user.id)
        db.session.delete(comment)
        db.session.commit()
        return {'Success': f'Comment ID: {comment_id} deleted'}
    else:
        return {'Error': 'Comment not found, please check reference and try again'}, 404



