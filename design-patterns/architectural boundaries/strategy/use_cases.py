from abc import ABC, abstractmethod
from typing import List, Optional
from presenters import NormalOrderPresenter, ReverseOrderPresenter


class Node:
    def __init__(self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.value = value
        self.left = left
        self.right = right


class AbstractTreeTravelrsal(ABC):
    @abstractmethod
    def traverse(self, root: Node) -> List[Node]:
        pass


class PreorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: str):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        if self.presenter == "normal":
            NormalOrderPresenter().present(self._recursive(root))
        elif self.presenter == "reverse":
            ReverseOrderPresenter().present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return [root.value] + self._recursive(root.left) + self._recursive(root.right)
        else:
            return []


class InorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: str):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        if self.presenter == "normal":
            NormalOrderPresenter().present(self._recursive(root))
        elif self.presenter == "reverse":
            ReverseOrderPresenter().present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return self._recursive(root.left) + [root.value] + self._recursive(root.right)
        else:
            return []


class PostorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: str):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        if self.presenter == "normal":
            NormalOrderPresenter().present(self._recursive(root))
        elif self.presenter == "reverse":
            ReverseOrderPresenter().present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return self._recursive(root.left) + self._recursive(root.right) + [root.value]
        else:
            return []
