##Pruebas de código

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

