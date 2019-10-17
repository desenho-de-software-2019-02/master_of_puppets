import mongoengine
import mongoengine.fields as fields

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop/skill')


class Skill(mongoengine.Document):
    meta = {'collection': 'mop_skills'}
    
    name = fields.StringField()
    usage_type = fields.StringField()
    description = fields.StringField()
    depends_on_skills = fields.ListField(fields.ReferenceField('Skill'))


class Proficiency(Skill):
    bonus = fields.IntField()


class Attack(Skill):
    attack_bonus = fields.IntField()
    attack_range = fields.IntField()
    attack_dices = fields.ListField(fields.ReferenceField('Dice'))


class Spell(Attack):
    level = fields.IntField()
    school = fields.StringField()
    casting_time = fields.IntField()
    duration = fields.IntField()
    is_verbal = fields.BooleanField()
    is_somatic = fields.BooleanField()
    is_material = fields.BooleanField()
