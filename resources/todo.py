from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import ToDoModel
from schemas import TodoSchema, PlainTodoSchema

blp = Blueprint("Todos","todos", description="Operation on Todos")

@blp.route("/create_todo")
class CreateTodo(MethodView):
    @blp.arguments(TodoSchema)
    def post(self, todo_data):
        todo = ToDoModel(**todo_data)

        db.session.add(todo)
        db.session.commit()

        return {"message":"Todo created successfully"}
    
@blp.route("/todo/<int:todo_id>")
class GetTodo(MethodView):
    @blp.response(200, TodoSchema)
    def get(self, todo_id):
        todo = ToDoModel.query.get_or_404(todo_id)

        return todo
    
    def delete(self, todo_id):
        todo = ToDoModel.query.get_or_404(todo_id)

        db.session.delete(todo)
        db.session.commit()

        return {"message":"Todo deleted successfully"}

@blp.route("/todos")
class ToDoList(MethodView):
    @blp.response(200, PlainTodoSchema(many=True))
    def get(self):
        todos = ToDoModel.query.all()

        return todos