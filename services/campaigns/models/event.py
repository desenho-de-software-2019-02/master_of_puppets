import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Event(mongoengine.Document):
    meta = {'collection': 'mop_events'}
    
    event_type = fields.StringField(required=True)
    description = fields.StringField(required=True)
    event_date = fields.StringField(required=True)
    data = fields.StringField(required=False)
