THIS_DIR := $(CURDIR)

build: 
	sudo docker-compose build

up: 
	sudo docker-compose up
back: 
	sudo docker-compose up resources campaigns

front: 
	sudo docker-compose up front
	
start-docker:
	systemctl start docker
