import dataclasses
from typing import Type, List


@dataclasses.dataclass
class Requirement:
    question: str
    response: str = ""


class UserRequirements:
    requirements: List[Requirement] = [
        Requirement(question="Wanna eat pizza or pasta?"),
        Requirement(question="Wanna drink coke or beer?"),
    ]


class Frontend:
    def __init__(self, requirements: Type[UserRequirements]):
        self.requirements = requirements.requirements

    def get_requirements_from_user(self):
        for requirement in self.requirements:
            requirement.response = input(requirement.question)
        return self.requirements

    def display_requirements(self):
        print("\nGathered requirements:")
        for req in self.requirements:
            print(f"Question: {req.question}, Response: {req.response}")


class Handler:
    def handle(self, req: Requirement):
        raise NotImplemented


class PizzaHandler(Handler):
    def handle(self, req: Requirement):
        print("make pizza")


class PastaHandler:
    def handle(self, req: Requirement):
        print("make pasta")


class CokeHandler:
    def handle(self, req: Requirement):
        print("bring coke")


class BeerHandler:
    def handle(self, req: Requirement):
        print("bring beer")


class DefaultHandler:
    def handle(self, req: Requirement):
        print(f"We cannot meet this req: {req.response}")


class Backend:
    def handle_requirements(self, reqs: List[Requirement]):
        response_action_mapping = {
            "pizza": PizzaHandler,
            "pasta": PastaHandler,
            "coke": CokeHandler,
            "beer": BeerHandler,
        }
        for req in reqs:
            response_action_mapping.get(req.response, DefaultHandler)().handle(req)


if __name__ == "__main__":
    """
    The main objective is to achieve high coherence and loose coupling.

    Adding new requirment is fairly simple: just add additional req to UserRequirements
    Adding new request handlers: add new response to response_action_mapping and new Handler class
    To modify the requirement just change the class and modify the logic how it will be handled.

    As you can see the main program execution logic is described within those couple of lines below.
    If there are no dependencies between the questions, even quite a complex logic can be implemented like that just if needed adding extra layer behind Handlers.
    If there will be a dependency between questions, then the Fronted and the Backend will need to cooperate in a loop something like:

    backEnd = Backend()
    reqs_empty = UserRequirements
    while True:
        frontEnd = Frontend(reqs_empty)
        reqs_filled = frontEnd.get_requirements_from_user()
        frontEnd.display_requirements(reqs_filled)

        response = backEnd.handle_requirements(reqs_filled)      
        reqs_empty = frontEnd.handle_response(response)
    """
    frontEnd = Frontend(UserRequirements)
    reqs = frontEnd.get_requirements_from_user()
    frontEnd.display_requirements()

    backEnd = Backend()
    backEnd.handle_requirements(reqs)

