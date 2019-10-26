import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Sheet(mongoengine.Document):
    meta = {'collection': 'mop_sheets'}
    
    name = fields.StringField(required=True)
