from fabric.api import run, local, hosts, cd
from fabric.contrib import django

#Lanzar app
def runapp():
	run('cd DAI2 && make run')