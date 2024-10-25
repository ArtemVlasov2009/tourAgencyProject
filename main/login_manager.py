import flask_login
from .settings import project
from user.models import Users

project.secret_key = 'T[,K[uhNm–fp50[l8uHn31_dRS]A0]'

login_manager = flask_login.LoginManager(app = project)

login_manager.init_app(project)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)