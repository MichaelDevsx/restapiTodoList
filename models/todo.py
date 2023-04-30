from db import db
from sqlalchemy import DateTime, func

class ToDoModel(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(DateTime(timezone=True), server_default=func.now())
    finish_date = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)

    project_id = db.Column(db.Integer(), db.ForeignKey("projects.id"), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    
    comment = db.relationship("CommentModel", backref="comments", lazy="dynamic")