from flask import Flask, render_template, json, request, session, redirect, url_for, Blueprint
from openGestion import db
from openGestion.users.forms import RegisterForm, LoginForm
from flask.ext.login import login_user, login_required, logout_user
from openGestion.users.models import User
from werkzeug import check_password_hash, generate_password_hash

#config with Blueprint
mod = Blueprint('users', __name__, 
    #url_prefix='/users',
    template_folder='templates')

@mod.route('/')
def homepage():
    return render_template('gestion.html')

@mod.route('/gestion')
def gestion():
	#return "OpenOrder"
    #return render_template('gestion.html')
    return render_template('singup.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    #form = LoginForm(request.form)
    form = LoginForm (csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user and check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('index'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(csrf_enabled=False)
    if form.validate_on_submit():
    #if request.method == 'POST' and form.validate():
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


@mod.route('/logout')
def logout():
    flask.session.pop('logged_in')
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('index'))