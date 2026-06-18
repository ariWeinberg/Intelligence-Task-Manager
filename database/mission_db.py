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
        stmt = """
        INSERT INTO `missions`
        (`title`, `description`, `location`,
        `difficulty`, `importance`, `status`,
        `risk_level`, `assigned_agent_id`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            data.mission_title,
            data.mission_description,
            data.mission_location,
            data.mission_difficulty,
            data.mission_importance,
            data.mission_status,
            data.risk_level(),
            data.mission_assigned_agent_id
        )
        
        with self.db_con() as cur:
            cur.execute(stmt, values)
            mission_id = cur.lastrowid

        return self.get_mission_by_id(mission_id) 

    def get_all_missions(self) -> list[MissionViewModel]:
        """Returns a list of all missions
        or an empty list if no missions exist.
        """
        stmt = """
        SELECT *
        FROM `missions`;
        """

        result: list[MissionViewModel] = []

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            for row in cur.fetchall():
                agent = MissionViewModel(**row)
                result.append(agent)

        return result
    
    def get_mission_by_id(self, id: int) -> MissionViewModel | None:
        """Returns a spesific mission's object
        by its id. or None if it doesn't exist.
        """
        stmt = """
        SELECT *
        FROM `missions`
        WHERE `id` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            return MissionViewModel(**cur.fetchone()) or None
    
    def assign_mission(self, m_id: int, a_id: int) -> str:
        """Assigns a mission to an agent,
        Returns a success \\ failure message.
        """
        stmt = """
            UPDATE `missions`
            SET
            `status` = 'ASSIGNED',
            `assigned_agent_id` = %s
            WHERE `id` = %s;
        """

        with self.db_con() as cur:
            cur.execute(stmt, (a_id, m_id,))

        return f"successfully assigned mission {m_id} to agent {a_id}"
    
    def update_mission_status(self, id: int, status: MissionStatus) -> str:
        """Updates the status of a mission by its mission's id
        to a given status, returns a success \\ failure message.
        """
        stmt = """
            UPDATE `missions`
            SET
            `status` = %s
            WHERE `id` = %s;
        """

        with self.db_con() as cur:
            cur.execute(stmt, (status, id,))

        return f"successfully changed the status of mission {id} to {status}."
    
    def get_open_missions_by_agent(self, id: int) -> list[MissionViewModel]:
        """Returns a list of all open missions (ASSIGNED \\ IN_PROGRESS)
        that are assigned to the agent with id.
        """
        stmt = """
        SELECT *
        FROM `missions`
        WHERE `assigned_agent_id` = %s
        AND
        (`status` = 'ASSIGNED' 
        OR
        `status` = 'IN_PROGRESS');
        """

        result: list[MissionViewModel] = []

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            for row in cur.fetchall():
                agent = MissionViewModel(**row)
                result.append(agent)

        return result
    
    def count_all_missions(self) -> int:
        """Returns the total count of all missions."""
        stmt = """
        SELECT COUNT(*) AS `total_missions`
        FROM `missions`;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            return cur.fetchone().get("total_missions", 0)
    
    def count_by_status(self,
                        status: MissionStatus
                        ) -> int:
        """Returns the total count of missions with a given status."""
        stmt = """
        SELECT COUNT(*) AS `total_missions`
        FROM `missions`
        WHERE `status` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (status, ))
            return cur.fetchone().get("total_missions", 0)
    
    def count_open_missions(self) -> int:
        """Returns the total count of open missions."""
        stmt = """
        SELECT COUNT(*) AS `total_missions`
        FROM `missions`
        WHERE (`status` = 'ASSIGNED' 
        OR
        `status` = 'IN_PROGRESS');
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            return cur.fetchone().get("total_missions", 0)
    
    def count_critical_missions(self) -> int:
        """Returns the total count of critical missions."""
        stmt = """
        SELECT COUNT(*) AS `total_missions`
        FROM `missions`
        WHERE `risk_level` = 'CRITICAL';
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            return cur.fetchone().get("total_missions", 0)
    
    def get_top_agent(self) -> AgentViewModel:
        """Returns the agent whom has completed the most missions."""
        stmt = """
            select * from agents
            ORDER BY agents.completed_missions DESC 
            LIMIT  1
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            return AgentViewModel(**cur.fetchone()) or None