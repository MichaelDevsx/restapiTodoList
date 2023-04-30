from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import ProjectModel
from schemas import ProjectSchema, PlainProjectSchema

blp = Blueprint("Projects","projects", description="Operation on projects")

@blp.route("/create_project")
class CreateProject(MethodView):
    @blp.arguments(ProjectSchema)
    def post(self, project_data):
        project = ProjectModel(**project_data)

        db.session.add(project)
        db.session.commit()

        return {"message": "Project created successfully"}, 200
    
@blp.route("/project/<int:project_id>")
class GetProject(MethodView):
    @blp.response(200, ProjectSchema)
    def get(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)

        return project
    
    def delete(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)

        db.session.delete(project)
        db.session.commit()

        return {"message":"Project deleted successfully"}
    
@blp.route("/projects")
class ProjectsList(MethodView):
    @blp.response(200, PlainProjectSchema(many=True))
    def get(self):
        projects = ProjectModel.query.all()
        
        return projects