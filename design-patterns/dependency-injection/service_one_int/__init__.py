from app import OneMaker


class ServiceOneInt(OneMaker):
    def __init__(self):
        self.name = "Service One Int"

    def __str__(self):
        return self.name

    def make_one(self) -> int:
        return 1
