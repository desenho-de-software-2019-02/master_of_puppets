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

event_model = api.model('Event', {
	'event_type': fields.String(required=True, description='Event type (e.g.: update)'),
	'description': fields.String(required=True, description='Event description'),
	'event_date': fields.String(required=True, description='Event datetime'),
	'data' : fields.String(required=False, description='JSON that might be related')
})


@api.route('/')
class EventList(Resource):
	@api.doc("Event List")
	def get(self):
		controller = get_controller()
		query = controller.list_elements()

		return jsonify(query)

	@api.doc("Event creation")
	@api.expect(event_model)
	def post(self):
		controller = get_controller()
		args = controller.new()

		return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Event not found')
@api.param('id', 'Event identifier')
class EventDetail(Resource):
	param = "An string that represents the event's id"

	@api.doc("Get information of a specific event", params={'id': param})
	@api.response(400, 'event not found')
	def get(self, id):
		controller = get_controller()

		try:
			event = controller.get_element_detail(id)
		except (DoesNotExist, ValidationError):
			api.abort(400, "Event with id {} does not exist".format(id))

		return json.loads(event)

	@api.doc("Update a event", params={'id': param})
	@api.expect(event_model)
	def put(self, id):
		controller = get_controller()

		try:
			new_event = controller.edit(id)
		except (DoesNotExist, ValidationError): 
			api.abort(400, "Event with id {} does not exist".format(id))

		return new_event

	@api.doc("Delete a event", params={'id': param})
	def delete(self, id):
		controller = get_controller()
		deleted = controller.delete(id)

		return deleted
		
