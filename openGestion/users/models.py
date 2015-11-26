from flask.ext.sqlalchemy import SQLAlchemy
from openGestion import db
#from app.users import constants as USER

#database model
class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        #self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name %r>' % self.name

#def get_id(self):
#        return unicode(self.id)