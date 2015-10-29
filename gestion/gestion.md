#Gestión de clientes


##Desarrollo de la aplicación
La aplicación está escrita en Python usando Flask. Por ello se han usado las siguientes herramientas para realizar los test necesarios y verificar el correcto funcionamiento así como la calidad de la misma:


 - Para el código Python **unittest** porque permite automatización de los test, tiene un uso sencillo, integración con Python y además es un paquete previamente instalado en Python y nos ahorra una instalación. 
 
 - Para Flask lo más sencillo es usar su propia herramienta **Werkzeug** que permite un uso en conjunto con *unittest*.


Para configurar el sistema de integración continúa y ya que todo el código se aloja en GitHub, Travis-CI es una buena herramienta para el testeo en este caso:




Travis

[![Build Status](https://travis-ci.org/nachobit/IV_PR_OpenOrder.svg?branch=master)](https://travis-ci.org/nachobit/IV_PR_OpenOrder)