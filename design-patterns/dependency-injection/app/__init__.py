from abc import ABC, abstractmethod


class OneMaker(ABC):
    @abstractmethod
    def make_one(self) -> int:
        pass


class TwoMaker(ABC):
    @abstractmethod
    def make_two(self) -> int:
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

