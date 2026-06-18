from typing import Literal
from database.db_connection import DBConnection
from models.agent_view_model import AgentViewModel
from models.mission_create_model import MissionCreateModel
from models.mission_view_model import MissionViewModel
from models.types import MissionStatus


class MissionDB:
    """A class that acts as an interface to the agents table (DAL)."""
    def __init__(self, connection_manager: DBConnection | None = None):
        """
        Initializes the interface and sets up a dbconnection for it.

        If a connection is provided it is used otherwise a new one is
            created with default settings.
        """
        self.db_con = connection_manager or DBConnection()

    def create_mission(self, data: MissionCreateModel) -> MissionViewModel:
        """Creates a new mission
        
        Returns the newly created mission's object (MissionView)
        """
        pass

    def get_all_missions(self) -> list[MissionViewModel]:
        """Returns a list of all missions
        or an empty list if no missions exist.
        """
        pass
    
    def get_mission_by_id(self, id: int) -> MissionViewModel:
        """Returns a spesific mission's object
        by its id. or None if it doesn't exist.
        """
        pass
    
    def assign_mission(self, m_id: int, a_id: int) -> str:
        """Assigns a mission to an agent,
        Returns a success \ failure message.
        """
        pass
    
    def update_mission_status(self, id: int, status: MissionStatus) -> str:
        """Updates the status of a mission by its mission's id
        to a given status, returns a success \ failure message.
        """
        pass
    
    def get_open_missions_by_agent(self, id: int) -> list[MissionViewModel]:
        """Returns a list of all open missions (ASSIGNED \ IN_PROGRESS)
        that are assigned to the agent with id.
        """
        pass
    
    def count_all_missions(self) -> int:
        """Returns the total count of all missions."""
        pass
    
    def count_by_status(self,
                        status: MissionStatus
                        ) -> int:
        """Returns the total count of missions with a given status."""
        pass
    
    def count_open_missions(self) -> int:
        """Returns the total count of open missions."""
        pass
    
    def count_critical_missions(self) -> int:
        """Returns the total count of critical missions."""
        pass
    
    def get_top_agent(self) -> AgentViewModel:
        """Returns the agent whom has completed the most missions."""
        pass
    