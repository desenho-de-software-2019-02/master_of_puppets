import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_controller import CharacterController

api = Namespace('characters', description='Character namespace')
