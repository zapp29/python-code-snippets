from use_cases import Node
from controller import Controller

tree = Node(value=1, left=Node(value=2, left=Node(value=4), right=Node(value=5)), right=Node(value=3, left=Node(value=6), right=Node(value=7)))


if __name__ == "__main__":
    Controller.get_tree_as_list(tree, "preorder", "normal")
