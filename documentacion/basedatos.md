##Creando una base de datos: PostgreSQL

Lo primero es añadir las dependencias que van a ser necesarias para enlazar nuestra aplicacón Flask con PostgreSQL en Heroku en el archivo [requirements](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/requirements.txt).

Lo siquiente será **crear una nueva base de datos** (1 gratis dentro del plan de desarrollo/prueba de Heroku):
 
```
heroku addons:create heroku-postgresql:hobby-dev
```
Y **establecer la base de datos como primaria**:
 
```
heroku pg:promote HEROKU_POSTGRESQL_COLOR
```

 - Creamos el archivo [config.py](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/config.py) que contiene las directrices para enlazar con la base de datos creada.

 - Añadimos al archivo principal de la aplicación [__init__.py](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/openGestion/__init__.py) las líneas:
 
```
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
```

Por tanto, una vez creada la base de datos, creado el archivo de configuración en la aplicación y añadidas las líneas anteriores, exportamos la [configuración](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/config.py) de la aplicación a Heroku:

```
export APP_SETTINGS="config.ProductionConfig"

heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku
```

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/bd5.png)

Y ```heroku config```:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/bd4.png)

Ya tendremos enlazada nuestra aplicación web con PostgreSQL en Heroku:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/db3.png)

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/db1.png)
