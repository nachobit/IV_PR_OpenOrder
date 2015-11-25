from flask import Flask, render_template, json, request, session, redirect, url_for
from wtforms import Form, BooleanField, TextField, PasswordField, validators
#from flask.ext.wtf import Form, BooleanField, TextField, PasswordField, validators
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import os, psycopg2

#PRUEBA MYSQL LOCAL
#mysql = MySQL()	//LOCAL
app = Flask(__name__)

#Postgre with SQL_ALQCHEMY
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get['DATABASE_URL', 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yebgaqukiltzzs:HE3SqSFyt09HOEtwsvedM7zJvv@ec2-54-83-203-50.compute-1.amazonaws.com:5432/d2qcb810h7i919'
#heroku = Heroku(app)
#db.init_app(app)
db = SQLAlchemy(app)

# MySQL configurations for LOCAL
#app.config['MYSQL_DATABASE_USER'] = 'nacho'
#app.config['MYSQL_DATABASE_PASSWORD'] = '1989+'
#app.config['MYSQL_DATABASE_DB'] = 'OpenGestion'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

#data = {}

class RegisterForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

@app.route('/')
def main():
    return render_template('gestion.html')

@app.route('/gestion')
def gestion():
	#return "OpenOrder"
    #return render_template('gestion.html')
    return render_template('singup.html')

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