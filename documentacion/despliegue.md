##HEROKU

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://opengestion.herokuapp.com)

Siguiendo el [tutorial de Python y Flask de Heroku](https://devcenter.heroku.com/articles/getting-started-with-python-o):

Lo primero es instalar [Heroku toolbelt](https://toolbelt.heroku.com) junto con *gunicorn* (Python Web Server Gateway Interface HTTP Server) previamente.

```
pip install gunicorn
```

- Una vez estamos registrados en Heroku y con el repositorio subido a GitHub, hacer *login* desde terminal:

```
heroku login
```
	
- Definir el archivo [Procfile](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/Procfile) para *decirle a Heroku que debe ejecutar*:
	
```
web: gunicorn gettingstarted.wsgi --log-file -
```

- Definir el archivo [requirements](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/requirements.txt) para que Heroku *reconozca la existencia de una aplicación*:

```
pip freeze > requirements.txt
```
Del fichero *requirements.txt* nos quedaremos solamente con las dependencias realmente necesarias con el fin de evitar problemas al lanzar Heroku.

```
Flask==0.10.1
Flask-MySQL==1.3
Jinja2==2.8
MarkupSafe==0.23
MySQL-python==1.2.5
Pygments==1.6
Werkzeug==0.10.4
altgraph==0.10.2
bdist-mpkg==0.5.0
gunicorn==19.3.0
itsdangerous==0.24
macholib==1.5.1
modulegraph==0.10.4
py2app==0.7.3
pyOpenSSL==0.13.1
pyparsing==2.0.1
python-dateutil==1.5
pytz==2013.7

```

Y por último:

```
wget -O- https://toolbelt.heroku.com/install.sh | sh
```
Que se resumen en realizar los pasos:

	1.  heroku create
		1.1 git add .
		1.2 git commit -m "Demo"
	2.	git push heroku master
	3.	heroku ps:scale web=1
	4.	heroku open
	
Para cualquier cambio que realicemos a partir de este punto en nuestra aplicación, bastará con realizar el *git push heroku master*.

Una vez realizados los pasos anteriores ya tendremos la aplicación perfectamente funcionando y corriendo sobre Heroku. Pero para conseguir que los cambios realizados se desplieguen al hacer ```git push ``` y continuar con la integración continua de la aplicación, enlazamos el repositorio con **Snap CI** y configuramos Heroku para trabajar con el Deploy Automático de Snap:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/snap.png)

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/heroCI.png)
	
Comprobamos nuestra aplicación funcionando correctamente en Heroku:

[Aplicación](https://opengestion.herokuapp.com)
