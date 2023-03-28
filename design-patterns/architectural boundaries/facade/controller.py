from use_cases import Node, PreorderTreeTravelrsal, InorderTreeTravelrsal, PostorderTreeTravelrsal


class Controller:
    @staticmethod
    def get_tree_as_list(root: Node, traverser: str, order: str) -> None:
        if traverser == "preorder":
            PreorderTreeTravelrsal(order).traverse(root)
        elif traverser == "inorder":
            InorderTreeTravelrsal(order).traverse(root)
        elif traverser == "postorder":
            PostorderTreeTravelrsal(order).traverse(root)
