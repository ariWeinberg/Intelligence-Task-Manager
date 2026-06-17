from contextlib import contextmanager
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector import connect


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
        self.host = host or "localhost"
        self.port = port or "3406"
        self.user = user or "root"
        self.password = password or "1234"
        self.database = database or 'Intelligence_db'

    def get_connection(self) -> MySQLConnectionAbstract:
        """
        Returns a connection to the server.

        Note that this method returns a connection to a spesific database.

        Caller MUST ensure the database exists.
        """
        return connect(host = self.host,
                       port = self.port,
                       user = self.user,
                       password = self.password,
                       database = self.database)

    def create_database(self) -> None:
        """
        Creates the database if it doesn't already exist.

        Note that this method uses its own connection to avoid trying to
            connect to a non-existant database.
        """
        connection = connect(host = self.host,
                       port = self.port,
                       user = self.user,
                       password = self.password)

        cur = connection.cursor()
        print(self.database)

        clean_database_name = (self.database if \
                               self.database.count(';') == 0 else None) or \
                                'Intelligence_db'
        database_creation_stmt = f"CREATE DATABASE IF NOT EXISTS \
            {clean_database_name};"
        cur.execute(database_creation_stmt)

        cur.close()
        connection.close()

    def create_tables(self) -> None:
        """
        Creates the tables needed for this app.

        The tables created by this method are: `agents` and `missions`. 

        Caller MUST ensure the database exists.
        """
        self._create_agents_table()
        self._create_missions_table()

    def _create_agents_table(self):
        """Creates the `agents` table needed for this app"""
        connection = self.get_connection()
        cur = connection.cursor()

        agents_table_creation_stmt = """CREATE TABLE IF NOT EXISTS `agents` (
        `id` INT AUTO_INCReMenT PRIMARY KEY,
        `name` VARCHAR(50) NOT NULL,
        `specialty` VARCHAR(50) NOT NULL,
        `is_active` BOOLEAN DEFAULT TRUE,
        `completed_missions` INT DEFAULT 0,
        `failed_missions` INT DEFAULT 0,
        `agent_rank` ENUM('Junior', 'Senior', 'Commander')
        );
        """
        cur.execute(agents_table_creation_stmt)
        cur.close()
        connection.close()

    def _create_missions_table(self):
        """Creates the `missions` table needed for this app"""
        connection = self.get_connection()
        cur = connection.cursor()

        missions_table_creation_stmt = """CREATE TABLE IF NOT EXISTS `missions` (
        `id` INT AUTO_INCReMenT PRIMARY KEY,
        `title` VARCHAR(50) NOT NULL,
        `description` TEXT NOT NULL,
        `location` VARCHAR(50) NOT NULL,
        `difficulty` INT NOT NULL,
        `importance` INT NOT NULL,
        `status` VARCHAR(11) DEFAULT 'NEW',
        `risk_level` VARCHAR(8),
        `assigned_agent_id` INT DEFAULT NULL
        );
        """
        cur.execute(missions_table_creation_stmt)
        cur.close()
        connection.close()

    @contextmanager
    def __call__(self, *args, **kwds):
        """
        Adds callability to every instance.
        
        Makes the instance act as a context manager yeilding an already
            initialized cursor and managing the connection afterwards.

        Ensures database creation.
        """
        self.create_database()
        connection = self.get_connection()
        cursor = connection.cursor(*args, **kwds)

        try:
            yield cursor
            connection.commit()
        except:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()
