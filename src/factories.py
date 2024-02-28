from src import settings
from src.abstract import AbstractDestination, AbstractSource
from src.destination.postgres.postgres import PostgresDestination
from src.source.input.input import Input


class TransferFactory:
    def __init__(self):
        self.src = settings.SOURCE
        self.dest = settings.DESTINATION

    def get_src(self) -> AbstractSource:
        if self.src == "input":
            return Input()
        if self.src == "slack":
            return ...
        if self.src == "tg":
            return ...
        if self.src == "discord":
            return ...
        raise ValueError

    def get_dest(self) -> AbstractDestination:
        if self.dest == "postgres":
            return PostgresDestination()
        raise ValueError
