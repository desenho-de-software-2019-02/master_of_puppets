import mongoengine
import mongoengine.fields as fields
import datetime
# from bson import ObjectID

mongoengine.connect('mop', host='mongo:27017')

class Campaign(mongoengine.Document):
    meta = {'collection': 'mop_matches', 'allow_inheritance': True}
    name = fields.StringField(required=True)
    gameMaster = fields.ObjectIdField(required=True)
    players = fields.ListField(fields.ObjectIdField())
    characters = fields.ListField(fields.ObjectIdField())
    rules = fields.ListField(fields.ObjectIdField())
    session = fields.ObjectIdField(required=True)
    initial_date = fields.DateTimeField(default=datetime.datetime.utcnow)