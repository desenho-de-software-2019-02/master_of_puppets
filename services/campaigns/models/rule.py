import mongoengine
import mongoengine.fields as fields


class Rule(mongoengine.Document):
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')

    meta = {'collection': 'mop_rule', 'db_alias': 'campaigns_connection'}

    name = fields.StringField(required=True)
    description = fields.StringField()
    races = fields.ListField()
    klasses = fields.ListField()
    skills = fields.ListField()
    items = fields.ListField()
