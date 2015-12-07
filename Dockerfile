FROM ubuntu:15.10
MAINTAINER Ignacio Romero Cabrerizo

#Instalar git y herramientas necesarias
RUN sudo apt-get -y update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential

#Clonar repositorio
RUN sudo git clone https://github.com/nachobit/IV_PR_OpenOrder.git

#Instalar requerimientos necesarios
RUN cd IV_PR_OpenOrder && git pull
RUN cd IV_PR_OpenOrder && make install