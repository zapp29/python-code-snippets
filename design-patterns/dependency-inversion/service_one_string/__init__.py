from app import OneMaker


class ServiceOneString(OneMaker):
    def __init__(self):
        self.name = "Service One String"

    def __str__(self):
        return self.name

    def make_one(self) -> str:
        return "1"
