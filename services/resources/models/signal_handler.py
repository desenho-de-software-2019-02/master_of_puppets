import datetime

from blinker import signal
from mongoengine import signals
import requests


class SignalHandler:
    """
    Class containing the functions that are triggered when an object is created or updated

    """

    CAMPAIGNS_SERVICE_URL = "http://localhost:9000/"
    EVENTS_URL_PATH = "events/"
    EVENT_DICT_TEMPLATE = dict(event_type=None, description=None, event_date=str(datetime.datetime.now()))

    def __init__(self):
        """
            Creates an update signal, as the create one is already provided by mongoengine
            and assign both to their respective handlers
        """
        self.update_signal = signal('update')
        self.update_signal.connect(self.object_update_handler)
        signals.post_save.connect(self.object_creation_handler)

    def object_update_handler(self, sender, **kwargs):
        event_dict = self._generate_dict('Update', **kwargs)
        self._send_request(event_dict)

    def object_creation_handler(self, sender, **kwargs):
        event_dict = self._generate_dict('Creation', **kwargs)
        self._send_request(event_dict)

    def _generate_dict(self, event_type, **kwargs):
        """
        Returns a dict that follows the Event class structure
        """
        event_dict = self.EVENT_DICT_TEMPLATE
        event_dict['event_type'] = event_type
        if event_type == 'Creation':
            event_dict['description'] = kwargs.get('document').to_json()
        else:
            event_dict['description'] = kwargs.get('document')

        return event_dict

    def _send_request(self, data):
        """
        Sends POST request to the campaigns service to create an Event entry
        """
        requests.post(self.CAMPAIGNS_SERVICE_URL + self.EVENTS_URL_PATH, json=data)
