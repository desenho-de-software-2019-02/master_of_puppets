import mongoengine
import mongoengine.fields as fields

# from pymongo import MongoClient
# client = MongoClient('mongo', 27017)
# db = client['mop']
# items_collection = db['mop_items']

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop')


# def insert_new_item(data):
#     new_element = {
#         "name": data["name"],
#         "description": data["description"],
#         "price": data["price"],
#         "weight": data["weight"]
#     }

#     result = items_collection.insert_one(new_element)
#     return str(result.inserted_id)


# class Item(mongoengine.Document):

#     def __init__(self, name, description, price, weight):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.weight = weight


class Item(mongoengine.Document):
    meta = {'collection': 'mop_items'}

    name = fields.StringField()
    description = fields.StringField()
    price = fields.DecimalField(min_value=0, precision=2)
    weight = fields.DecimalField(min_value=0, precision=2)


class Armor(Item):
    weapon_type = fields.StringField()
    # 32bit integer field, for 64 use LongField()
    armor_class_mod = fields.IntField()
    armor_class_max = fields.IntField()


class Weapon(Item):
    dmg_dice = fields.ReferenceField('Dice')
    weapon_type = fields.StringField()


class EffectItem(Item):
    # only differs from Item on methods
    pass
