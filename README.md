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

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/pane2.png)

---

##Enlazado con Base de Datos: PostgreSQL
Este proyecto se va a enlazar con una base de datos [PostGres](http://postgresapp.com) de [Heroku](https://www.heroku.com/postgres) para el manejo de las sesiones de usuarios y datos asociados a la aplicación web.

Para ello se hará uso de [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/).

[Documento](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/documentacion/basedatos.md)

---

#Integración Continua

La integración continua se ha realizado sobre el primer desarrollo del CRM de gestión de clientes enlazando con la base de datos y donde se ha creado un acceso interno mediante *login* para administrar los datos e información relativa:

###Pruebas de código: unittest y Travis
La aplicación está escrita en Python usando Flask. Por ello se han usado las siguientes herramientas para realizar los test necesarios y verificar el correcto funcionamiento así como la calidad de la misma:

 - Para el código Python: `unittest`, ya permite automatización de los test, tiene un uso sencillo, integración con Python y además es un paquete previamente instalado en Python y nos ahorra una instalación. 
 
 - Para Flask lo más sencillo es usar su propia herramienta *Werkzeug* que permite un uso en conjunto con *unittest*.

Para configurar el sistema de integración continúa y ya que todo el código se aloja en GitHub, *Travis-CI* es una buena herramienta para el testeo en este caso. 

[Documento](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/documentacion/integracioncont.md)
 
---

#Despliegue de la aplicación en un PaaS
###HEROKU

Para el despliegue de la aplicación se va a usar [Heroku](https://www.heroku.com/) como PaaS (Platform as a Service), debido a su gran integración con GitHub y la facilidad de uso. Además permite el despliegue de aplicaciones de forma gratuita, a pesar de tener algunas restricciones, será suficiente para nuestro proyecto.

[Documento](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/documentacion/despliegue.md)

---

#Entorno de Pruebas
###DOCKER

La idea detrás de [Docker](https://www.docker.com) es crear contenedores ligeros y portables para las aplicaciones software que puedan ejecutarse en cualquier máquina con Docker instalado, independientemente del sistema operativo que la máquina tenga por debajo, facilitando así también los despliegues. A diferencia de una máquina virtual, no requiere incluir un sistema operativo independiente.

[Documento](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/documentacion/entornopruebas.md)

---

#Despliegue de la aplicación en un IaaS
###AZURE

Se ha realizado el despliegue automático de la aplicación en [Azure](http://azure.microsoft.com) mediante el uso de [Vagrant](https://www.vagrantup.com) y [Ansible](http://www.ansible.com) como gestores de configuración. Concretamente:

**Vagrant** es una herramienta para la creación y configuración de entornos de desarrollo virtualizados.

**Ansible** es una plataforma de software libre para configurar y administrar computadoras. Para nuestro despliegue hará de *provisionador*.

[Documento](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/documentacion/azure.md)
