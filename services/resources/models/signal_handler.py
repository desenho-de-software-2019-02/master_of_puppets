from blinker import signal
from mongoengine import signals
import requests


class SignalHandler:

    def __init__(self):
        self.update_signal = signal('update')
        self.update_signal.connect(self.object_update_handler)
        signals.post_save.connect(self.object_creation_handler)

    @staticmethod
    def object_update_handler(sender, **kwargs):
        pass

    @staticmethod
    def object_creation_handler(sender, **kwargs):
        pass


