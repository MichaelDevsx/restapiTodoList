from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import CommentModel
from schemas import CommentSchema, PlainCommentSchema

blp = Blueprint("Comments","comments", description="Operation on comments")

@blp.route("/create_comment")
class CreateComment(MethodView):
    @blp.arguments(CommentSchema)
    def post(self, comment_data):
        comment = CommentModel(**comment_data)
        
        db.session.add(comment)
        db.session.commit()

        return {"message": "Comment created"}

@blp.route("/comment/<int:comment_id>")
class GetComment(MethodView):
    @blp.response(200, CommentSchema)
    def get(self, comment_id):
        comment = CommentModel.query.get(comment_id)

        return comment
    
    def delete(self, comment_id):
        comment = CommentModel.query.get(comment_id)

        db.session.delete(comment)
        db.session.commit()

        return {"message": "Comment deleted"}

@blp.route("/comments")
class GetCommentList(MethodView):
    @blp.response(200, CommentSchema(many=True))
    def get(self):
        comment = CommentModel.query.all()

        return comment