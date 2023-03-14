from typing import Type
from app import AbstractServiceFactory, TMaker


class ServiceFactory(AbstractServiceFactory):
    @staticmethod
    def make_service(service: Type[TMaker]) -> TMaker:
        return service()
