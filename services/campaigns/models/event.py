import mongoengine
import mongoengine.fields as fields


class Event(mongoengine.Document):
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')

    meta = {'collection': 'mop_events', 'db_alias': 'campaigns_connection'}

    name = fields.StringField(required=True)
