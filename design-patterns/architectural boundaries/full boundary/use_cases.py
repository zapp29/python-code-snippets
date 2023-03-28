from abc import ABC, abstractmethod
from typing import List, Optional


class Node:
    def __init__(self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.value = value
        self.left = left
        self.right = right


class AbstractTreeTravelrsal(ABC):
    @abstractmethod
    def traverse(self, root: Node) -> List[Node]:
        pass


class AbstractPresenter(ABC):
    @abstractmethod
    def present(self, tree: List[int]) -> None:
        pass


class PreorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: AbstractPresenter):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        self.presenter.present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return [root.value] + self._recursive(root.left) + self._recursive(root.right)
        else:
            return []


class InorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: AbstractPresenter):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        self.presenter.present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return self._recursive(root.left) + [root.value] + self._recursive(root.right)
        else:
            return []


class PostorderTreeTravelrsal(AbstractTreeTravelrsal):
    def __init__(self, presenter: AbstractPresenter):
        self.presenter = presenter

    def traverse(self, root: Node) -> None:
        self.presenter.present(self._recursive(root))

    def _recursive(self, root: Node) -> List[int]:
        if root:
            return self._recursive(root.left) + self._recursive(root.right) + [root.value]
        else:
            return []
