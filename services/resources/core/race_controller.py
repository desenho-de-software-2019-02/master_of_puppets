from models.race_model import insert_new_race, list_race, delete_race_db,update_race_db, get_race

def create_race(data):
    #validar dados 
    return insert_new_race(data)


def get_race_list():
    return list_race()

def delete_race(data):
    id  = data["_id"]
    return delete_race_db(id)


def update_race(data):
    return update_race_db(data)

def read_race(id):
    
    result = get_race(id)
    result["_id"]= str(result["_id"])
    return result