import mongoengine
import mongoengine.fields as fields


class Event(mongoengine.Document):
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')
    meta = {'collection': 'mop_events', 'db_alias': 'campaigns_connection'}
    
    event_type = fields.StringField(required=True)
    description = fields.StringField(required=True)
    event_date = fields.StringField(required=True)
    data = fields.StringField(required=False)
