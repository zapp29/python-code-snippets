from use_cases import AbstractTreeTravelrsal, Node


class Controller:
    @staticmethod
    def get_tree_as_list(root: Node, traverser: AbstractTreeTravelrsal) -> None:
        traverser.traverse(root)
