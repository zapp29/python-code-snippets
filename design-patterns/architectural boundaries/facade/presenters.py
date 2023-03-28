from typing import List


class NormalOrderPresenter:
    def present(self, list_of_objects: List[int]) -> None:
        print(list_of_objects)


class ReverseOrderPresenter:
    def present(self, list_of_objects: List[int]) -> None:
        print(list_of_objects[::-1])
