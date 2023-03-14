from abc import ABC, abstractmethod
from typing import Type, Union


class OneMaker(ABC):
    @abstractmethod
    def make_one(self) -> int:
        pass


class TwoMaker(ABC):
    @abstractmethod
    def make_two(self) -> int:
        pass


TMaker = Union[OneMaker, TwoMaker]


class AbstractServiceFactory(ABC):
    @staticmethod
    @abstractmethod
    def make_service(service: Type[TMaker]) -> TMaker:
        pass


class AbstractAppFactory(ABC):
    @staticmethod
    @abstractmethod
    def make_app(name: str, one_maker: Type[TMaker], two_maker: Type[TMaker]) -> "App":
        pass


class App:
    def __init__(self, name, one_maker: OneMaker, two_maker: TwoMaker):
        self.name = name
        self.one_maker = one_maker
        self.two_maker = two_maker

    def run(self) -> None:
        one = self.one_maker.make_one()
        two = self.two_maker.make_two()
        print(f"{self.name} is running {one} and {two}")
