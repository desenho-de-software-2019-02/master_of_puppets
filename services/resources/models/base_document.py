import mongoengine

from models.signal_handler import SignalHandler


class BaseDocument(mongoengine.Document):
    meta = {'abstract': True}
    signal_handler = SignalHandler()

    def update(self, **kwargs):
        """
        This variation emits a signal with the help of the blinker package
        """
        no_docs_updated = super().update(**kwargs)
        self.signal_handler.update_signal.send(self, **kwargs)
        return no_docs_updated
