#Gestión de clientes


##Pruebas de código
La aplicación está escrita en Python usando Flask. Por ello se han usado las siguientes herramientas para realizar los test necesarios y verificar el correcto funcionamiento así como la calidad de la misma:


 - Para el código Python: **unittest**, ya permite automatización de los test, tiene un uso sencillo, integración con Python y además es un paquete previamente instalado en Python y nos ahorra una instalación. 
 
 - Para Flask lo más sencillo es usar su propia herramienta **Werkzeug** que permite un uso en conjunto con *unittest*.
 
	+ Se crea un archivo *test.py* en el mismo directorio de *app.py* (archivo de Flask que general el entorno web).
	
	+ Se importa *unittest* y crean algunos test para verificar el código.
 
 ```
import unittest
from app import app
from flask import Flask, render_template

def fun(x):
    return x + 1

class TestCode(unittest.TestCase):
    def test_code(self):
        self.test_app = app.test_client()
        #self.test_app = app.test_client()
        
        #Test demo
        self.assertEqual(fun(3), 4)

        #Test Response is 200 OK
        response = self.test_app.get('/gestion', follow_redirects=True)
        self.assertEqual(response.status, " OK")

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
 
 ![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/testq.png)
 


Para configurar el sistema de integración continúa y ya que todo el código se aloja en GitHub, Travis-CI es una buena herramienta para el testeo en este caso:




Travis

[![Build Status](https://travis-ci.org/nachobit/IV_PR_OpenOrder.svg?branch=master)](https://travis-ci.org/nachobit/IV_PR_OpenOrder)