from db import db
from sqlalchemy import DateTime, func

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(DateTime(timezone=True), server_default=func.now())
    finish_date = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)