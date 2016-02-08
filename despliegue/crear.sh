#!/bin/bash
	
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
	
vagrant up --provider=azure

fab -H vagrant@baresnacho-service-gkdzg.cloudapp.net runapp