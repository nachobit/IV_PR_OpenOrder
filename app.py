from flask import Flask, render_template, json, request, session, redirect, url_for
from wtforms import Form, BooleanField, TextField, PasswordField, validators
#from flask.ext.login import login_user, login_required, logout_user
#from project.models import User, bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import os, psycopg2
#from models import *

#PRUEBA MYSQL LOCAL
#mysql = MySQL()	//LOCAL
app = Flask(__name__)

#Postgre with SQL_ALQCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919'
#db.init_app(app)
db = SQLAlchemy(app)

# MySQL configurations for LOCAL
#app.config['MYSQL_DATABASE_USER'] = 'nacho'
#app.config['MYSQL_DATABASE_PASSWORD'] = '1989+'
#app.config['MYSQL_DATABASE_DB'] = 'OpenGestion'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

#data = {}

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Length(min=1, max=25)])

class RegisterForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        #self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<Name %r>' % self.name


def get_id(self):
        return unicode(self.id)


@app.route('/')
def main():
    return render_template('gestion.html')

@app.route('/gestion')
def gestion():
	#return "OpenOrder"
    #return render_template('gestion.html')
    return render_template('singup.html')

@app.route('/login')
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('index'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    #if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('singup.html', form=form)


@app.route('/logout')
def logout():
    flask.session.pop('logged_in')
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')