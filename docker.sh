#!/bin/bash

#Descargar la imagen
sudo docker pull nachobit/iv_pr_openorder
#Ejecuta la imagen
sudo docker run -i -t nachobit/iv_pr_openorder /bin/bash