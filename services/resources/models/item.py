import mongoengine
import mongoengine.fields as fields

from models.base_document import BaseDocument


class ItemFactory:
    def __init__(self, json_data):
        self.json_data = json_data

    def _clean_fields(self, fields):
        for field in fields:
            self.json_data.pop(field, None)

    def get_data(self):
        return self.json_data

    def create_item(self):
        """
        Returns an instance to a CommonItem, Armor or Weapon,
        depending on the fields given by the request
        """

        if self.json_data.get('weapon_type') is not None:
            if all(self.json_data.get(field) is not None for field in ['armor_class_mod', 'armor_class_max']):
                self._clean_fields(['dmg_dice'])
                return Armor()
            elif self.json_data.get('dmg_dice') is not None:
                self._clean_fields(['armor_class_mod', 'armor_class_max'])
                return Weapon()
            else:
                raise ValueError('Invalid arguments')
        else:
            self._clean_fields(['weapon_type', 'armor_class_mod', 'armor_class_max', 'dmg_dice'])
            return CommonItem()


class CommonItem(BaseDocument):
    def __str__(self):
        return 'CommonItem'

    meta = {'collection': 'mop_items', 'allow_inheritance': True}

    name = fields.StringField(required=True)
    description = fields.StringField(required=True)
    price = fields.DecimalField(required=True, min_value=0, precision=2)
    weight = fields.DecimalField(required=True, min_value=0, precision=2)


class Armor(CommonItem):
    def __str__(self):
        return 'Armor'

    weapon_type = fields.StringField(required=True)
    # 32bit integer field, for 64 use LongField()
    armor_class_mod = fields.IntField(required=True)
    armor_class_max = fields.IntField(required=True)


class Weapon(CommonItem):
    def __str__(self):
        return 'Weapon'

    dmg_dice = fields.StringField(required=True)
    weapon_type = fields.StringField(required=True)
    proficiency = fields.IntField(required=True)

class EffectItem(CommonItem):
    # only differs from Item on methods
    pass
