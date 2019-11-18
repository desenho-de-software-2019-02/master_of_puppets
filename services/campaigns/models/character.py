import mongoengine
import mongoengine.fields as fields


class Character(mongoengine.Document):
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')

    meta = {'collection': 'mop_characters', 'db_alias': 'campaigns_connection'}

    user = fields.StringField(required=True)
    character_sheet = fields.StringField(required=True)
    campaign = fields.ObjectIdField(required=True)
    character_mementoes = fields.ListField(fields.StringField())
