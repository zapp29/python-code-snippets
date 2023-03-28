from typing import List
from use_cases import AbstractPresenter


class NormalOrderPresenter(AbstractPresenter):
    def present(self, list_of_objects: List[int]) -> None:
        print(list_of_objects)


class ReverseOrderPresenter(AbstractPresenter):
    def present(self, list_of_objects: List[int]) -> None:
        print(list_of_objects[::-1])
