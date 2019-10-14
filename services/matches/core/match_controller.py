from models.match import matchModel

class matchController:
    def create_match(data):

        # Validar os dados do character
        return matchModel.create_new_match(data) 

    def get_matches():
        return matchModel.list_matches()

    def get_match_master(gameMaster):
        list_match = gameMaster_matchs(gameMaster)
        if list_match:
            return list_match
        return 'This master no have match'

    def delete_match(data):
        id = data['_id']
        return matchModel.delete_match(id)

