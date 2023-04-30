from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)

    project = db.relationship("ProjectModel", backref="users", lazy="dynamic")
    todo = db.relationship("ToDoModel", backref="users", lazy="dynamic")
    comment = db.relationship("CommentModel", backref="users", lazy="dynamic")