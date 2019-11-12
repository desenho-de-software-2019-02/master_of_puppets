import mongoengine
from mongoengine.queryset import OperationError


class BaseDocument(mongoengine.Document):
    meta = {'abstract': True}

    def update(self, **kwargs):
        """
        This variation emits a signal with the help of the blinker package
        """
        no_docs_updated = super().update(**kwargs)
        print("Document updated") # TODO: Add actual signal activity
        return no_docs_updated

