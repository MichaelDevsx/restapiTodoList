from db import db
from sqlalchemy import DateTime, func

class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    start_date = db.Column(DateTime(timezone=True), server_default=func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    todo_id = db.Column(db.Integer(), db.ForeignKey("todos.id"), nullable=False)