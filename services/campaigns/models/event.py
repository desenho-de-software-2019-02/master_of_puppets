import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Event(mongoengine.Document):

    meta = {'collection': 'mop_events'}

    name = fields.StringField(required=True)
