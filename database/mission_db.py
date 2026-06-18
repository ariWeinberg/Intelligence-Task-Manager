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

    def create_mission(data) : 
        """Creates a new mission
        
        Returns the newly created mission's object (MissionView)
        """
        pass

    def get_all_missions() :
        """Returns a list of all missions
        or an empty list if no missions exist.
        """
        pass
    
    def get_mission_by_id(id):
        """Returns a spesific mission's object
        by its id. or None if it doesn't exist.
        """
        pass
    
    def assign_mission(m_id, a_id):
        """Assigns a mission to an agent,
        Returns a success \ failure message.
        """
        pass
    
    def update_mission_status(id, status):
        """Updates the status of a mission by its mission's id
        to a given status, returns a success \ failure message.
        """
        pass
    
    def get_open_missions_by_agent(id):
        """Returns a list of all open missions (ASSIGNED \ IN_PROGRESS)
        that are assigned to the agent with id.
        """
        pass
    
    def count_all_missions(): 
        """Returns the total count of all missions."""
        pass
    
    def count_by_status(status):
        """Returns the total count of missions with a given status."""
        pass
    
    def count_open_missions(): 
        """Returns the total count of open missions."""
        pass
    
    def count_critical_missions(): 
        """Returns the total count of critical missions."""
        pass
    
    def get_top_agent():
        """Returns the agent whom has completed the most missions."""
        pass
    