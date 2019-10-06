from models.match import insert_new_match

def validate_match(data):

    # Validar os dados do character
    if insert_new_match(data)

def get_match():
    return read_match()

def get_match_master(gameMaster):
    list_match = gameMaster_matchs(gameMaster)
    if list_match:
        return list_match
    return 'This master no have match'

