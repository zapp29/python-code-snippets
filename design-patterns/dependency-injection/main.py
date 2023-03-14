from typing import Type

from app import App, TMaker, AbstractAppFactory
from services import ServiceFactory
from services.service_one_int import ServiceOneInt
from services.service_two_int import ServiceTwoInt
from services.service_one_string import ServiceOneString
from services.service_two_string import ServiceTwoString


class AppFactory(AbstractAppFactory):
    @staticmethod
    def make_app(name: str, one_maker: Type[TMaker], two_maker: Type[TMaker]) -> App:
        return App(
            name,
            ServiceFactory.make_service(one_maker),
            ServiceFactory.make_service(two_maker)
        )


if __name__ == "__main__":
    app = AppFactory.make_app("App1", ServiceOneInt, ServiceTwoInt)
    app.run()
