import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.event_controller import EventController

from models.event import Event

api = Namespace('events', description='Event namespace')

def get_controller():
	controller = EventController(model=Event, request=request)
	return controller
