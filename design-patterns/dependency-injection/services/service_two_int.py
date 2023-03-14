from app import TwoMaker


class ServiceTwoInt(TwoMaker):
    def __init__(self):
        self.name = "Service Two Int"

    def __str__(self):
        return self.name

    def make_two(self) -> int:
        return 2
