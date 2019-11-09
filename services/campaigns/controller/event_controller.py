from json import dumps
from json import loads
from models.event import Event

from flask_restplus import reqparse


class EventController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Create new event
        """
        parser = reqparse.RequestParser()
        parser.add_argument('description', required=True)
        parser.add_argument('event_type', required=True)
        parser.add_argument('event_date', required=True)
        parse_result = parser.parse_args(req=self.request)

        Event.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all events
        """

        list_of_events = list(map(lambda event: loads(event.to_json()), Event.objects.all()))
        
        return list_of_events

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an event campaigning the given id
        """

        return Event.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits an event given its id
        """
        event = Event.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('description', required=True)
        parser.add_argument('event_type', required=True)
        parser.add_argument('event_date', required=True)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = event.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(event.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an event given its id
        """
        target = Event.objects.get(id=identifier)
        target_data = loads(target.to_json())
        
        target.delete()

        return target_data
