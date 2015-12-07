test:
	python -m unittest test_u
.PHONY: test

install:
	sudo apt-get update 
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

heroku:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	heroku login
	heroku create
	git add .
	git commit -m "despliegue heroku"
	git push heroku master
	heroku ps:scale web=1
	heroku open

run:
	python run.py