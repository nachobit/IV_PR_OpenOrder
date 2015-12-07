##DOCKER

Para instalar **docker** en ubuntu debemos ejecutar: ``` sudo apt-get install docker.io ```

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/docker1.png)

Una vez hecho esto se deben realizar los siguientes pasos: 

- Crear el archivo [Dockerfile]() 
- Registrarse en [DockerHub](https://hub.docker.com)
	- Crear un *Automated Build* de nuestro repositorio enlazado de *GitHub*
	
![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/hub.png)
	
Ya tendremos nuestra aplicación en Docker:

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/practica/docker2.png)

- Solo falta lanzar el [script]() que automatiza las siguientes tareas:
	
	- Descargar la imagen: ``` docker pull nachobit/iv_pr_openorder ```
	- Ejecutar la imagen: ``` sudo docker run -i -t nachobit/iv_pr_openorder /bin/bash ```


