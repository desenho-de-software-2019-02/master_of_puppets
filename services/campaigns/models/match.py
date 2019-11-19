import mongoengine
import mongoengine.fields as fields
import datetime


class Match(mongoengine.Document):
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')

    meta = {'collection': 'mop_matches', 'db_alias': 'campaigns_connection'}

    name = fields.StringField(required=True)
    battles = fields.ListField(fields.ReferenceField('Combat'))
    events = fields.ListField(fields.ReferenceField('Event'))
    date = fields.DateTimeField(default=datetime.datetime.utcnow)
    description = fields.StringField()
    campaign = fields.ReferenceField('Campaign', required=True)
