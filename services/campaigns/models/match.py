import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Match(mongoengine.Document):
    meta = {'collection': 'mop_matches'}

    name = fields.StringField(required=True)
    events = fields.ListField(fields.ReferenceField('Event'))
    date = fields.DateTimeField(required=True)
    description = fields.StringField()
    
