THIS_DIR := $(CURDIR)

back: 
	sudo docker-compose up resources matches

front: 
	sudo docker-compose up front

fs:
	sudo docker-compose up

start-docker:
	systemctl start docker
