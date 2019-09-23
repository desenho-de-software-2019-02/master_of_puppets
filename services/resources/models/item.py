from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
items_collection = db['mop_items']


def insert_new_item(data):
    new_element = {
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "weight": data["weight"]
    }

    items_collection.insert_one(new_element)
