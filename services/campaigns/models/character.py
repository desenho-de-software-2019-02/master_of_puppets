import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Character(mongoengine.Document):
    meta = {'collection': 'mop_characters'}

    user = fields.StringField(required=True)
    character_sheet = fields.StringField(required=True)
    character_mementoes = fields.ListField(fields.StringField())
