from contextlib import contextmanager
from mysql.connector.abstracts import MySQLConnectionAbstract


class DBConnection:
    def __init__(self,
                 host: str | None = None,
                 port: str | None = None,
                 user: str | None = None,
                 password: str | None = None,
                 database: str | None = None
                 ):
        pass

    def get_connection(self) -> MySQLConnectionAbstract:
        pass

    def create_database(self) -> None:
        pass

    def create_tables(self) -> None:
        pass

    @contextmanager
    def __call__(self, *args, **kwds):
        pass
