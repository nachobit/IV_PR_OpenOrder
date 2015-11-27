import os, sys
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
#app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919'


from openGestion.users import views

#register blueprints
#from app.users.views import mod
from openGestion.users.views import mod as usersModule
#app.register_blueprint(mod)
app.register_blueprint(usersModule)

from openGestion.users.models import User
login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
