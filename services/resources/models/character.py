from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
characters_collection = db['mop_characters']


def insert_new_character(data):
    new_element = {
        "id": data["id"]
    }
    print("passou")
    characters_collection.insert_one(new_element)