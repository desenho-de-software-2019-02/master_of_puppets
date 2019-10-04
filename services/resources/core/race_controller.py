from models.race_model import insert_new_race, read_race

def create_race(data):
    #validar dados 
    return insert_new_race(data)


def get_race():
    return read_race()
