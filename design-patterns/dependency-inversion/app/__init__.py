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
    def __init__(self, name):
        self.name = name

    def run(self, one_maker: OneMaker, two_maker: TwoMaker) -> None:
        one = one_maker.make_one()
        two = two_maker.make_two()
        print(f"{self.name} is running {one} and {two}")

