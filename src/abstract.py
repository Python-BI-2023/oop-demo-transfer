from abc import ABC, abstractmethod
from typing import Iterable

from src.types import Data


class AbstractSource(ABC):
    @abstractmethod
    def read_data(self) -> Iterable[Data]:
        raise NotImplementedError

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class AbstractDestination(ABC):
    @abstractmethod
    def write_data(self, data: Data):
        raise NotImplementedError

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError
