from pymongo import MongoClient
from flask_api import status
# from bson import ObjectID


client = MongoClient('mongo', 27017)
db = client['mop']
match_collection = db['mop_match']

class matchModel:

    def create_new_match(data):
        new_element = {
            "gameMaster": data["gameMaster"],
            "players": data["players"],
            "characters": data["characters"],
            "rules": data["rules"],
            "session": data["session"],
            "date_initial": data["session"]
        }   
        print(match_collection.insert_one(new_element))
        return status.HTTP_201_CREATED
        return status.HTTP_400_BAD_REQUEST

    def list_matches():
        matchs = []
        all_matchs = match_collection.find() 
        for match in all_matchs:
            element = {
                "gameMaster": match["gameMaster"],
                "players": match["players"],
                "characters": match["characters"],
                "rules": match["rules"],
                "session": match["session"],
                "date_initial": match["session"]
            }
            matchs.append(element)         
        return matchs, status.HTTP_200_OK
    #WIP
    # def delete_match(id):
    #     match_collection.delete_one({'_id': ObjectId(id)})

    def gameMaster_matchs(name):
        all_matchs = match_collection.find()
        match_gameMaster = []
        for match in all_match:
            if match['gameMaster'] == name:
                match_gameMaster.append(match)
        if match_gameMaster:
            return "This master has no matches"
        return match_gameMaster
