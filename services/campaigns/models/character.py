import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Character(mongoengine.Document):
    meta = {'collection': 'mop_characters'}
    
    name = fields.StringField(required=True)
