THIS_DIR := $(CURDIR)

build: 
	sudo docker-compose build

up: 
	sudo docker-compose up
back: 
	sudo docker-compose up resources campaigns services

front: 
	sudo docker-compose up front

fs:
	sudo docker-compose up

start-docker:
	systemctl start docker
