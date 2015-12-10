##DOCKER

Para instalar **docker** en ubuntu debemos ejecutar: ``` sudo apt-get install docker.io ```

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/docker1.png)

Para crear el contenedor Docker se deben realizar los siguientes pasos (como se indica [aquí](https://docs.docker.com/docker-hub/builds/)): 

- Crear el archivo [Dockerfile](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/Dockerfile) 
- Registrarse en [DockerHub](https://hub.docker.com)
	- Crear un *Automated Build* de nuestro repositorio enlazado de *GitHub*
	
![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/hub.png)

En la opción *Build Settings* indicamos el Tag (latest) al que realizar el build. 
	
Ya tendremos Docker configurado con el *Dockerfile*:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/hub1.png)

Y el repositorio enlazado y ejecutando en el contenedor:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/hub2.png)

- Solo falta lanzar el [script](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/docker.sh) que automatiza las siguientes tareas:
	
	- Descargar la imagen: ``` docker pull nachobit/iv_pr_openorder ```
	- Ejecutar la imagen: ``` sudo docker run -i -t nachobit/iv_pr_openorder /bin/bash ```


[Docker imagen](https://hub.docker.com/r/nachobit/iv_pr_openorder/)
