from database.db_connection import DBConnection


class MissionDB:
    """A class that acts as an interface to the agents table (DAL)."""
    def __init__(self, connection_manager: DBConnection | None = None):
        """
        Initializes the interface and sets up a dbconnection for it.

        If a connection is provided it is used otherwise a new one is
            created with default settings.
        """
        self.db_con = connection_manager or DBConnection()
