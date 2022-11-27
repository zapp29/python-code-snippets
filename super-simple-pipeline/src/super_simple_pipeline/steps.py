import abc
from typing import Any, Optional, Dict


class PreFetcher(abc.ABC):
    @abc.abstractmethod
    def run(self) -> Optional[Dict[str, Any]]:
        return {}


class DataFetcher(abc.ABC):
    @abc.abstractmethod
    def run(self, data) -> Optional[Dict[str, Any]]:
        return {}


class PostProcessor(abc.ABC):
    @abc.abstractmethod
    def run(self, data) -> Optional[Dict[str, Any]]:
        return {}
