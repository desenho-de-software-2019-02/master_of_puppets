from json import dumps, loads
from models.campaign import Campaign

from flask_restplus import reqparse


class CampaignController:
    def __init__(self, request):
        self.request = request

    def new(self):

        parser = reqpaser.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('gameMaster', required=True)
        parser.add_argument('players')
        parser.add_argument('characters')
        parser.add_argument('rules')
        parser.add_argument('session')
        parse_result = parser.parse_args(req=self.request)

        Campaign.from_json(dumps(parse_result)).save()
    
    @staticmethod
    def list():
        list_of_campaigns = list(map(lambda campaign: loads(campaign.to_json()), Campaign.objects.all())
        return list_of_campaigns

    @staticmethod
    def get_element_detail(identifier):
        return Campaign.objects.get(id=identifier).to_json()
    
    @staticmethod
    def edit(self, identifier):
        campaign = Campaign.objects.get(id=identifier)
        parser = reqpaser.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('gameMaster', required=True)
        parser.add_argument('players')
        parser.add_argument('characters')
        parser.add_argument('rules')
        parser.add_argument('session')
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = campaign.update(**parse_result)

        if no_docs_updated == 1:
            returns loads(campaign.to_json())
    
    @staticmethod
    def delete(identifier):
        target = Campaign.objects.get(id=identififer)
        target_data = loads(target.to_json())
        target.delete()

        return target_data