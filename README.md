# Proyecto IV - openGestion - #

[![Build Status](https://travis-ci.org/nachobit/IV_PR_OpenOrder.svg?branch=master)](https://travis-ci.org/nachobit/IV_PR_OpenOrder)

[![Build Status](https://snap-ci.com/nachobit/IV_PR_OpenOrder/branch/master/build_image)](https://snap-ci.com/nachobit/IV_PR_OpenOrder/branch/master)

##Autor e integrante del repositorio 
 - Ignacio Romero Cabrerizo

##Este repositorio pertenece al Proyecto Global: OpenOrder
Proyecto para la gestión de pedidos de pequeña a mediana empresa mediante una aplicación cliente-servidor. El servidor hará de intermediario entre 2 clientes (comercio y usuario) con notificaciones push. El usuario podrá realizar un pedido directamente a través de la aplicación y el comercio será notificado, agilizando el proceso de comunicación entre ambas partes.

##Integrantes del proyecto global
- **Ignacio Romero Cabrerizo**
- Jose Ignacio Recuerda Cambil
- Antonio Miguel Pozo Cámara

##Descripción de la aplicación
Creación de una aplicación web *CRM* (Customer Relationship Management) para la gestión de clientes y de los comercios asociados. Se encargará de crear un modelo de gestión de "usuarios" con el fin de obtener:

 - Automatización y promoción de ventas
 - Seguimiento personalizado desde la primera toma de contacto con el cliente
 - Aprovechar los recursos implícitos en la base de datos de estos clientes
 - Atención al cliente y reporte de incidencias

##Infraestructura Virtual
La aplicación será accesible desde cualquier navegador. 

Se desarrolla con **Flask** (Python) y contendrá una **base de datos MySQL**. 

Para su despliegue se utilizará **Heroku (como PaaS)**. 

Se usarán también herramientas proporcionadas por **ZOHO (como SaaS)** para inclusión de chat en la aplicación.

---
#Integración Continua

La integración continua se ha realizado sobre el primer desarrollo del CRM de gestión de clientes enlazando con la base de datos y donde se ha creado un acceso interno mediante *login* para administrar los datos e información relativa:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/pane1.png)


![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/pane2.png)

##Pruebas de código
La aplicación está escrita en Python usando Flask. Por ello se han usado las siguientes herramientas para realizar los test necesarios y verificar el correcto funcionamiento así como la calidad de la misma:


 - Para el código Python: `unittest`, ya permite automatización de los test, tiene un uso sencillo, integración con Python y además es un paquete previamente instalado en Python y nos ahorra una instalación. 
 
 - Para Flask lo más sencillo es usar su propia herramienta *Werkzeug* que permite un uso en conjunto con *unittest*.
 
###unittest

 * Se crea un archivo *test.py* en el mismo directorio de *app.py* (archivo de Flask que general el entorno web).
	
 * Se importa *unittest* y crean algunos test para verificar el código.
 
 ```
import unittest
from app import app
from flask import Flask, render_template

def fun(x):
    return x + 1

class TestCode(unittest.TestCase):
    def test_code(self):
        self.test_app = app.test_client()
        
        #Test demo
        self.assertEqual(fun(3), 4)

        #Test Response is 200 OK
        response = self.test_app.get('/gestion', follow_redirects=True)
        self.assertEqual(response.status, "200 OK")

        # Test logging out
        logout = self.test_app.get('/logout', follow_redirects=True)
        #assert 'You were logged out' in logout.data

if __name__ == '__main__':
    unittest.main()
 
 ```
 Para probar *unittest* basta con escribir el comando:
 
 ```
 python -m unittest test
```

Podemos automatizar esta tarea (lanzar test) creando un **makefile** que contenga las sentencias para lanzar la batería de test:

```
test:
	python -m unittest test_u
.PHONY: test
```
 Y simplemente con **make** realizar el test:
 
![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/make.png)
 
 
 En el primer caso se realiza la verificación correcta. En el segundo caso modificando uno de los `assert` se observa cómo el código falla al lanzar el test:
 
![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/testq.png)
 
De igual forma si la `base de datos` no está correctamente enlazada o funcionando lanzará un error:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/error.png)


###Travis

Para configurar el sistema de integración continúa y ya que todo el código se aloja en GitHub, *Travis-CI* es una buena herramienta para el testeo en este caso:

Se crea el archivo de configuración de travis (.travis.yml):

```
language: python

python:
  - "2.7"

install:
  - pip install flask-mysql

script: nosetests
```

Y un archivo setup.py:

```
from setuptools import setup

setup(name='openGestion',
	version='0.0.1',
	description='Aplicación web CRM para el manejo de clientes',
	url='https://github.com/nachobit/IV_PR_OpenOrder',
	author='Ignacio Romero Cabrerizo',
	author_email='nachorc@correo.ugr.es',
	license='GNU General Public License',
	packages=['openGestion'],
	install_requires=[
		'Flask',
	],
	zip_safe=False)
```

Y se configura desde la propia web de forma que verifique la integridad del repositorio en futuras modificaciones.

---

##DESPLIEGUE DE LA APLICACIÓN EN UN PAAS
###HEROKU

Para el despliegue de la aplicación se va a usar HEROKU como PaaS (Platform as a Service), debido a su gran integración con GitHub y la facilidad de uso. Además permite el despliegue de aplicaciones de forma gratuita, a pesar de tener algunas restricciones, será suficiente para nuestro proyecto.

Los siguientes pasos tras instalar *Heroku toolbelt* junto con *gunicorn* (Python Web Server Gateway Interface HTTP Server) previamente:

Una vez registrado en Heroku y con el repositorio subido a GitHub, hacer *login* desde terminal:

```
heroku login
```
	
- Definir el archivo **Procfile** para `decirle Heroku que debe ejecutar`:
	
```
web: gunicorn gettingstarted.wsgi --log-file -
```

- Definir el archivo **requirements.txt** para que Heroku reconozca la existencia de una aplicación:

```
pip freeze > requirements.txt
```
Del fichero *requirements* nos quedaremos solamente con las dependencias realmente necesarias con el fin de evitar problemas al lanzar Heroku.

Y por último:

	1.  heroku create
	2.	git push heroku master
	3.	heroku ps:scale web=1
	4.	heroku open
	
Para cualquier cambio que realicemos a partir de este punto en nuestra aplicación, bastará con realizar el *git push heroku master*.

Una vez realizados los pasos anteriores ya tendremos la aplicación perfectamente funcionando y corriendo sobre Heroku. Pero para conseguir que los cambios realizados se desplieguen al hacer ```git push ``` y continuar con la integración continua de la aplicación, enlazamos el repositorio con **Snap CI** y configuramos Heroku para trabajar con el Deploy Automático de Snap:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/snap.png)

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/heroCI.png)
	
Comprobamos nuestra aplicación funcionando correctamente en Heroku:

[Aplicación](https://calm-mountain-1223.herokuapp.com)

---