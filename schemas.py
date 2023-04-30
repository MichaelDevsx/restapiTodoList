from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class PlainProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.String(required=True)
    start_date = fields.Date()
    finish_date = fields.String()

class PlainTodoSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    start_date = fields.Date()
    finish_date = fields.String()
    status = fields.Str()

class PlainCommentSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.String()
    start_date = fields.Date()

class UserSchema(PlainUserSchema):
    project = fields.List(fields.Nested(PlainProjectSchema()),dump_only=True)
    todo = fields.List(fields.Nested(PlainTodoSchema()),dump_only=True)
    comment = fields.List(fields.Nested(PlainCommentSchema()),dump_only=True)

class ProjectSchema(PlainProjectSchema):
    user_id = fields.Int(load_only=True)
    todos_id = fields.List(fields.Nested(PlainTodoSchema()),dump_only=True)

class TodoSchema(PlainTodoSchema):
    project_id = fields.Int(load_only=True)
    user_id = fields.Int(load_only=True)
    comment = fields.List(fields.Nested(PlainCommentSchema()),dump_only=True)

class CommentSchema(PlainCommentSchema):
    user_id = fields.Int(load_only=True)
    todo_id = fields.Int(load_only=True)