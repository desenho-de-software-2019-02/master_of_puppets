import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.event_controller import EventController

from models.event import Event
from services.base_controller import Context
api = Namespace('events', description='Event namespace')


def get_controller():
	controller = Context(strategy=EventController(), model=Event, request=request)
	return controller

