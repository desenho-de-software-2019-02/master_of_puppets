import datetime

from blinker import signal
from mongoengine import signals
import requests


class SignalHandler:
    """
    Class containing the functions that are triggered when an object is created or updated

    """

    CAMPAIGNS_SERVICE_URL = "http://localhost:5001/"
    EVENTS_URL_PATH = "events/"
    EVENT_DICT_TEMPLATE = dict(event_type=None, event_date=str(datetime.datetime.now()), data=None)

    def __init__(self):
        """
            Creates an update signal, as the create one is already provided by mongoengine
            and assign both to their respective handlers
        """
        self.update_signal = signal('update')
        self.update_signal.connect(self.object_update_handler)
        signals.post_save.connect(self.object_creation_handler)

    def object_update_handler(self, sender, **kwargs):
        event_dict = self._generate_dict('Update', sender, **kwargs)
        self._send_request(event_dict)

    def object_creation_handler(self, sender, **kwargs):
        event_dict = self._generate_dict('Creation', sender, **kwargs)
        self._send_request(event_dict)

    def _generate_dict(self, event_type, sender, **kwargs):
        """
        Returns a dict that follows the Event class structure
        """
        event_dict = self.EVENT_DICT_TEMPLATE
        event_dict['event_type'] = event_type
        event_dict['description'] = sender._class_name
        if event_type == 'Creation':
            event_dict['data'] = kwargs.get('document').to_json()
        else:
            event_dict['data'] = kwargs.get('document')

        return event_dict

    def _send_request(self, data):
        """
        Sends POST request to the campaigns service to create an Event entry
        """
        try:
            print(data)
            requests.post(self.CAMPAIGNS_SERVICE_URL + self.EVENTS_URL_PATH, json=data)
        except requests.exceptions.ConnectionError as err:
            # Changing to a logging lib solution would be great
            print(err)
            print("Unable to connect to the campaigns service, event creation failed")
