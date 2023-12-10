from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required
from flask import request, Blueprint
from init import db
from blueprints.auth_bp import owner_admin_authorize

bp_comments = Blueprint("bp_comments",__name__, url_prefix='/comments')


@bp_comments.route('/')
@jwt_required()
def read_all_comments():
    stmt = db.select(Comment)
    comments = db.session.scalars(stmt).all()
    return CommentSchema(many=True).dump(comments)

@bp_comments.route('/<int:id>')
@jwt_required()
def read_one_comment(id):
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        owner_admin_authorize(comment.id)
        return CommentSchema().dump(comment)
    else:
        return {'Error': 'Comment not found'}, 404


@bp_comments.route('/', methods=['POST'])
@jwt_required()
def create_comments():
    comment_info = CommentSchema(exclude=['id']).load(request.json)
    
    comment = Comment(
        message = comment_info.get('message'),
        activity_id = comment_info.get('activity_id')
    )

    db.session.add(comment)
    db.session.commit()

    return CommentSchema().dump(comment), 201



@bp_comments.route('/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
def edit_comments(id):
    comment_info = CommentSchema(exclude=['id']).load(request.json)
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        owner_admin_authorize(comment.id)
        comment.message = comment_info.get('message', comment.message)
        comment.activity_id = comment_info.get('activity_id', comment.activity_id)

        db.session.commit()

        return CommentSchema().dump(comment)
   
    else:
        return {'Error': 'Comment not found'}, 404

#Delete a comment
@bp_comments.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_comments(id):
    stmt= db.select(Comment).filter_by(id = id)
    comment= db.session.scalar(stmt)
    if comment:
        owner_admin_authorize(comment.id)
        db.session.delete(comment)
        db.session.commit()
        return {'Success': f'Comment ID: {id} and all related content deleted'}
