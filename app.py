from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
#from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'nacho'
app.config['MYSQL_DATABASE_PASSWORD'] = '1989+'
app.config['MYSQL_DATABASE_DB'] = 'OpenGestion'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

data = {}

@app.route('/')
def main():
    return render_template('gestion.html')

@app.route('/gestion')
def gestion():
	#return "OpenOrder"
    #return render_template('gestion.html')
    return render_template('singup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@app.route('/logout')
def logout():
    flask.session.pop('logged_in')
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')