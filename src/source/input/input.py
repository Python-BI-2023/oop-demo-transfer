from typing import Iterable

from src.abstract import AbstractSource
from src.types import Data


class Input(AbstractSource):
    def read_data(self) -> Iterable[Data]:
        data = input("Введите данные через запятую: source, name, email, text\n")
        parsed_data = []
        for line in data.split("|"):
            source, name, email, text = line.split(",")
            parsed_data.append(Data(source=source, name=name, email=email, text=text))
        return parsed_data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
