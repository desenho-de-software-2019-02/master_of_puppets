from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mop']
match_collection = db['mop_match']


def insert_new_match(data):
    new_element = {
        "gameMaster": data["gameMaster"],
        "players": data["players"],
        "characters": data["characters"],
        "rules": data["rules"],
        "session": data["session"],
        "date_initial": data["session"]
    }   

    match_collection.insert_one(new_element)