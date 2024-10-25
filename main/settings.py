
import flask, flask_sqlalchemy, flask_migrate


import flask
import  flask_sqlalchemy
import flask_migrate

project = flask.Flask(
    import_name = "main",
    template_folder = "templates"
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db = DATABASE)



