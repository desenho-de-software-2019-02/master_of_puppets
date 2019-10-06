from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mop']
match_collection = db['mop_match']

def validate_match3(data):
    if data["players"] is not []:
        return True
    return False

def create_new_match(data):
    if validate_match(data):
        new_element = {
            "gameMaster": data["gameMaster"],
            "players": data["players"],
            "characters": data["characters"],
            "rules": data["rules"],
            "session": data["session"],
            "date_initial": data["session"]
        }   
        match_collection.insert_one(new_element)
        return "Sucessfully create"
    return "Failed to create"

def read_match():
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
        matchs.append(info) 
    
    if matchs == []:
        return "there are no matchs yet"
    return matchs

def gameMaster_matchs(name):
    all_matchs = match_collection.find()
    match_gameMaster = []
    for match in all_match:
        if match['gameMaster'] == name:
            match_gameMaster.append(match)
    if match_gameMaster:
        return "This master has no matches"
    return match_gameMaster
