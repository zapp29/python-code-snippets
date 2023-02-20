from app import TwoMaker


class ServiceTwoString(TwoMaker):
    def __init__(self):
        self.name = "Service Two String"

    def __str__(self):
        return self.name

    def make_two(self) -> str:
        return "2"
