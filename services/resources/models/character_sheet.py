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
    dexterity = fields.FloatField()
    constitution = fields.FloatField()
    intelligence = fields.FloatField()
    wisdom = fields.FloatField()
    charisma = fields.FloatField()
    race = fields.StringField()
    character_class = fields.StringField()
    skills = fields.ListField(fields.StringField())
    items = fields.ListField(fields.StringField())
    owner = fields.StringField()
    # race = fields.ReferenceField('Race')
    # character_class = fields.ReferenceField('CharacterClass')
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
    level = fields.IntField()
    experience = fields.LongField()
    strength = fields.FloatField()
    dexterity = fields.FloatField()
    constitution = fields.FloatField()
    intelligence = fields.FloatField()
    wisdom = fields.FloatField()
    charisma = fields.FloatField()
    skills = fields.ListField(fields.StringField())
    items = fields.ListField(fields.StringField())
    date = fields.DateTimeField()
