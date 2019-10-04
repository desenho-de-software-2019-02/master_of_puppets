from models.race_model import insert_new_race, read_race, delete_race_db,update_race_db

def create_race(data):
    #validar dados 
    return insert_new_race(data)


def get_race():
    return read_race()

def delete_race(data):
    name  = data["name"]
    return delete_race_db(name)


def update_race(data):
    return update_race_db(data)