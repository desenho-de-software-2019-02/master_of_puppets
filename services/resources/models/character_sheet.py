import mongoengine
import mongoengine.fields as fields
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits



class CharacterSheet(mongoengine.Document):
    name = fields.StringField()
    description = fields.StringField()
    hit_points = fields.IntField()
    level = fields.IntField()
    experience = fields.LongField()
    strength = fields.FloatField()
    desterity = fields.FloatField()
    costitution = fields.FloatField()
    intelligence = fields.FloatField()
    wisdom = fields.FloatField()
    charisma = fields.FloatField()
    race = fields.StringField()
    klass = fields.StringField()
    skills = fields.ListField(fields.StringField())
    items = fields.ListField(fields.StringField())
    owner = fields.StringField()
    # race = fields.ReferenceField('Race')
    # klass = fields.ReferenceField('Klass')
    # skills = fields.ListField(fields.ReferenceField('Skill'))
    # items = fields.ListField(fields.ReferenceField('Item'))
    # owner = fields.ReferenceField('User')


    def restore(self, memento):
        """
        Restores the Originator's state from a memento object.
        """
        
        self.hit_points = memento.get_hit_points()
        self.update()

class ConcreteCharacterMemento(mongoengine.Document):
    
    hit_points = fields.IntField()    
    date = fields.DateTimeField()