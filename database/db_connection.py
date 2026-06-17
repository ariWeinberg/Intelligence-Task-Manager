from contextlib import contextmanager
from mysql.connector.abstracts import MySQLConnectionAbstract


class DBConnection:
    """DBConnection is a simple mysql connection and server manager."""
    def __init__(self,
                 host: str | None = None,
                 port: str | None = None,
                 user: str | None = None,
                 password: str | None = None,
                 database: str | None = None
                 ):
        """Initializes the manager, by setting its parameters."""
        pass

    def get_connection(self) -> MySQLConnectionAbstract:
        """
        Returns a connection to the server.

        Note that this method returns a connection to a spesific database.

        Caller MUST ensure the database exists.
        """
        pass

    def create_database(self) -> None:
        """
        Creates the database if it doesn't already exist.

        Note that this method uses its own connection to avoid trying to
            connect to a non-existant database.
        """
        pass

    def create_tables(self) -> None:
        """
        Creates the tables needed for this app.

        The tables created by this method are: `agents` and `missions`. 

        Caller MUST ensure the database exists.
        """
        pass

    @contextmanager
    def __call__(self, *args, **kwds):
        """
        Adds callability to every instance.
        
        Makes the instance act as a context manager yeilding an already
            initialized cursor and managing the connection afterwards.

        Ensures database creation.
        """
        pass
