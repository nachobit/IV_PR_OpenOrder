##AZURE

[![Azure](http://azuredeploy.net/deploybutton.png)](baresnacho-service-gkdzg.cloudapp.net:8000/rango)

###Despliegue automático
La forma automática de realizar el despliegue completo de la aplicación y dejarla funcionando en una MV de Azure es con un *script* como el siguiente:

```
	#!/bin/bash
	
	vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
	
	vagrant up --provider=azure
```

Tambíen se puede lanzar mediante la utilidad **Fabric** con la orden descrita en un [fabfile.py](https://github.com/nachobit/IV_PR_OpenOrder/fabfile.py):

```fab -H vagrant@baresnacho-service-gkdzg.cloudapp.net runapp```

###Configuración completa (pasos a seguir)
Los pasos a seguir para poder realizar el despliegue automático en Azure con el script anterior son los siguientes:

 - Instalar *VirtualBox, Vagrant y AzureCLI* en caso de no tenerlos previamente instalados como se ha visto [aquí](https://github.com/nachobit/IV-2015-16/blob/master/ejercicios/IgnacioRomeroCabrerizo/ejercicios5.md).

 - Instalar Vagrant Azure Provider:
 
 	``` vagrant plugin install vagrant-azure ```
 	
	 ![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/tema6/vazure.png)
	 
 - Realizar el *login* en Azure siguiendo los pasos indicados: 	
 	1. azure login
 	2. azure config mode asm
	3. azure account download
	4. Descargar el fichero tras iniciar sesión en el link mostrado en terminal	
	![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/tema5/azure4.png)
	5. azure account import archivo-descargado
 
 - Obtener el *"id"* de nuestra cuenta en Azure para el siguiente paso:
 
 	![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/tema6/idazure.png)
 	
 	- Para la gestión de certificados, necesarios para autenticar en Azure, crear las claves **.pem** y **.cer** necesarias:
 
 	```
 	mkdir ~/Documentos/clave
 	
 	openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout ~/Documentos/clave/azure.pem -out ~/Documentos/clave/azure.pem

	openssl x509 -inform pem -in ~/Documentos/clave/azure.pem -outform der -out ~/Documentos/clave/azure.cer
	
 	``` 	 	
 
 - Subir el archivo **.cer** creado en el paso anterior en Azure:
 
	![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/tema6/az1.png)
	
	Ya tendremos correctamente "certificado" el acceso.
	
 - Crear el [**ansible_hosts**](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/despliegue/ansible_host):
 	
 	``` 
 	[azure]
	maquina-nacho-ubu.cloudapp.net
	[localhost]
	192.168.56.10
	```
 
 - Crear el archivo de configuración de *Ansible*, en este caso [**vdeploy.yml**](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/despliegue/vdeploy.yml):
 	
 ```
- hosts: localhost

  become: yes
  become_method: sudo
  remote_user: vagrant

  tasks:
  - name: Actualizar
    apt: update_cache=yes upgrade=dist
  - name: Instalar paquetes
    apt: name=python-setuptools state=present
    apt: name=build-essential state=present
    apt: name=python-dev state=present
    apt: name=git state=present
    
  - name: Instalar pip
    action: apt pkg=python-pip

  - name: Clonar repositorio de git
    git: repo=https://github.com/nachobit/DAI_bares.git  dest=DAI2 clone=yes force=yes
  
  - name: Permisos de ejecucion al directorio
    file: path=DAI2 state=touch mode="u+rw"

  - name: Instalar requisitos
    shell: cd DAI2 && make install

  - name: ejecutar
    command: nohup sudo python DAI2/manage.py runserver 0.0.0.0:8000
    register: errores
  
  - debug: msg="{{ errores.stdout }}"
  - debug: msg="{{ errores.stderr }}"
 	
 ```
 
 - Crear el [**Vagrantfile**](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/despliegue/Vagrantfile) que creará la MV en Azure y la configurará de forma automática:
 
```Vagrant.configure(2) do |config|  config.vm.box = "azure"  # Create a forwarded port mapping which allows access to a specific port  # within the machine from a port on the host machine. In the example below,  # accessing "localhost:8080" will access port 80 on the guest machine.  config.vm.network "forwarded_port", guest: 8000, host: 8000  # Create a private network, which allows host-only access to the machine  # using a specific IP.  config.vm.network "private_network", ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"  # Create a public network, which generally matched to bridged network.  # Bridged networks make the machine appear as another physical device on  # your network.  config.vm.network "public_network"  config.vm.define "localhost" do |l|    l.vm.hostname = "localhost"  end    # Provider-specific configuration so you can fine-tune various  # backing providers for Vagrant. These expose provider-specific options.  # Example for VirtualBox:  #  config.vm.provider "azure" do |azure|
  azure.mgmt_certificate = File.expand_path('~/Documents/Virtual/openG/clave/azure.pem')
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = 'd6bbcf1a-b999-4eab-934d-cd3a395a90cf'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
    azure.vm_name = 'baresnacho'
    azure.vm_password = 'Clave#Nacho#1'
    azure.vm_location = 'Central US'
    azure.ssh_port = '22'
    azure.tcp_endpoints = '80:80'
  end  # Enable provisioning with a shell script. Additional provisioners such as  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the  # documentation for more information about their specific syntax and use.  config.vm.provision "ansible" do |ansible|    ansible.sudo = true      ansible.playbook = "vdeploy.yml"      ansible.verbose = "v"      ansible.host_key_checking = false    endend 
       
```

 - Exportamos la variable de entorno de Ansible para que se reconozca los host:

	``` export ANSIBLE_HOSTS=~/ansible_hosts ```
  
 ---
 
 Por último realizamos los mismos pasos que el *script* inicial: 
  
 - Crear un "box" con una imagen de azure:
 
 	```vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box```
 	
 - Crear la máquina con:
 	```vagrant up --provider=azure```
 	
 __NOTA__
 
 En el caso de disponer de la máquina creada bastaría con: ```vagrant provision```

![img](https://github.com/nachobit/ETSIIT/blob/master/backup/IV1516/ejercicios/tema6/vg2.png)

La aplicación estará andando en la VM de Azure como se puede ver [aquí](http://baresnacho-service-gkdzg.cloudapp.net:8000/rango/).