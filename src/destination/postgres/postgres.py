import psycopg2

from src import settings
from src.abstract import AbstractDestination
from src.destination.postgres.sql_queries import INSERT_DATA
from src.types import Data


class PostgresDestination(AbstractDestination):
    def __init__(self):
        self._conn = None
        self._cur = None

    def write_data(self, data: Data):
        self._cur.execute(
            query=INSERT_DATA,
            vars=data.to_dict(),
        )

    def __enter__(self):
        self._conn = psycopg2.connect(
            host=settings.POSTGRES_DESTINATION_CREDS["host"],
            database=settings.POSTGRES_DESTINATION_CREDS["dbname"],
            user=settings.POSTGRES_DESTINATION_CREDS["user"],
            password=settings.POSTGRES_DESTINATION_CREDS["password"],
            port=settings.POSTGRES_DESTINATION_CREDS["port"],
        )
        self._conn.autocommit = True
        self._cur = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cur.close()
        self._conn.close()
