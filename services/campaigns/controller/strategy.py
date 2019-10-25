from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():

    def __init__(self, strategy: Strategy, request, model):
        self._strategy = strategy
        self.request = request
        self.model = model

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def get_unique(identifier):
        return self.model.objects.get(id=identifier)
    
    def new(self):
        parser = self._strategy.set_parser()
        parse_result = parser.parse_args(req=self.request)
        self.model.from_json(dumps(parse_result)).save()
        return parse_result

    def list(self):
        list_of_elements = list(map(lambda element: loads(element.to_json()), self.model.objects.all()))
        return list_of_elements

    def get_element_detail(self, identifier):
        return get_unique(identifier).to_json()
    
    def edit(self, identifier):
        element = get_unique(identifier)
        parser = self._strategy.set_parser()
        parse_result = parser.parse_args(req=self.request)
        no_docs_updated = element.update(**parse_result)
        if no_docs_updated == 1:  # the row was updated successfully
            return loads(self.model.to_json())
        
    def delete(self, identifier):
        target = get_unique(identifier)
        target_data = loads(target.to_json())
        target.delete()
        return target_data
        
class Strategy(ABC):
    @abstractmethod
    def set_parser(self):
        pass

class CampaignController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('gameMaster', required=True)
        self.parser.add_argument('players', action='append')
        self.parser.add_argument('characters', action='append')
        self.parser.add_argument('rules', action='append')
        self.parser.add_argument('session')
        return self.parser

class MatchController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('events', action='append')
        self.parser.add_argument('description')
        return self.parser
    



if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(strategy=MatchController(), model=Match, request=request)
    print("Client: Strategy is set to match.")
    context.new()
    print()

    context = Context(strategy=CampaignController(), model=Campaign, request=request)
    print("Client: Strategy is set to campaign.")
    context.new()