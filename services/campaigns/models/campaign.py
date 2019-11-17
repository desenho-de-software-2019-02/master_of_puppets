import mongoengine
import mongoengine.fields as fields
import datetime
# from bson import ObjectID

mongoengine.connect('mop', host='mongo:27017')

class Campaign(mongoengine.Document):

    meta = {'collection': 'mop_campaigns', 'allow_inheritance': True}
    
    gameMaster = fields.StringField(required=True)
    name = fields.StringField(required=True)
    players = fields.ListField(fields.StringField())
    characters = fields.ListField(fields.StringField())
    rules = fields.ListField(fields.StringField())
    initial_date = fields.DateTimeField(default=datetime.datetime.utcnow)
