from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
#app.secret_key = "somethingelse-else"
app.config.from_object('config')
#app.config.from_object('config.BaseConfig')

#configuration db
import os
#app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)	#object

#app.config['SQLALCHEMY_DATABASE_URI'] = ''


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
