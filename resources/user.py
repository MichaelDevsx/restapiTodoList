from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt, jwt_required
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema,PlainUserSchema
from blocklist import BLOCKLIST

blp = Blueprint("Users","users", description="Operation on users")

@blp.route("/register")
class CreateUser(MethodView):
    @blp.arguments(PlainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message = "User already exists" )
        
        user = UserModel(
            name = user_data["name"],
            email = user_data["email"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message":"User created successfully"}, 201

@blp.route("/user/<int:user_id>")
class GetUser(MethodView):
    @blp.response(200, UserSchema())
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        
        db.session.delete(user)
        db.session.commit()

        return {"message":"User deleted successfully"}

@blp.route("/users")
class GetUserList(MethodView):
    @blp.response(200, PlainUserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users
    
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity = user.name, fresh=True)
            refresh_token = create_refresh_token(identity = user.name)
            return {"access_token":access_token, "refresh_token": refresh_token}
        abort(401, message="Invalid Credentials.")

@blp.route("/logout")
class UserLogout(MethodView):
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully logged out"},200