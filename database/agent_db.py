from database.db_connection import DBConnection
from models.agent_create_model import AgentCreateModel
from models.agent_view_model import AgentViewModel


class AgentDB:
    """A class that acts as an interface to the agents table (DAL)."""
    def __init__(self, connection_manager: DBConnection | None = None):
        """
        Initializes the interface and sets up a dbconnection for it.

        If a connection is provided it is used otherwise a new one is
            created with default settings.
        """
        self.db_con = connection_manager or DBConnection()

    def create_agent(self, data: AgentCreateModel) -> AgentViewModel:
        """Creates a new agent in the table (a new row)."""
        stmt = """
        INSERT INTO `agents`
        (`name`, `specialty`, `agent_rank`)
        VALUES (%s, %s, %s);
        """
        values = (
            data.agent_name,
            data.agent_specialty,
            data.agent_agent_rank
        )
        
        with self.db_con() as cur:
            cur.execute(stmt, values)
            agent_id = cur.lastrowid

        return self.get_agent_by_id(agent_id) 

    def get_all_agents(self) -> list[AgentViewModel]:
        """Returns a list of all agents."""
        stmt = """
        SELECT *
        FROM `agents`;
        """

        result: list[AgentViewModel] = []

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            for row in cur.fetchall():
                try:
                    agent = AgentViewModel(**row)
                    result.append(agent)
                except:
                    pass

        return result

    def get_agent_by_id(self, id: int) -> AgentViewModel | None:
        """Returns the agent with a matching id."""
        stmt = """
        SELECT *
        FROM `agents`
        WHERE `id` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            return AgentViewModel(**cur.fetchone()) or None

    def update_agent(self, id: int, data: AgentCreateModel) -> str:
        """Applys the update data to the agent with a matching id."""
        stmt = """
        UPDATE `agents`
        SET
        `name` = %s,
        `specialty` = %s,
        `is_active` = %s,
        `completed_missions` = %s,
        `failed_missions` = %s,
        `agent_rank` = %s
        WHERE `id` = %s;
        """
        values = (
            data.agent_name,
            data.agent_specialty,
            data.agent_is_active,
            data.agent_completed_missions,
            data.agent_failed_missions,
            data.agent_agent_rank,
            id
        )
        
        with self.db_con() as cur:
            cur.execute(stmt, values)
            agent_id = cur.lastrowid

        return f"successfully updated agent {id}."

    def deactivate_agent(self, id: int) -> str:
        """Deactivates an agent."""
        stmt = """
        UPDATE `agents`
        SET
        `is_active` = FALSE
        WHERE `id` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
        return f"Successfully deactivated agent {id}."

    def increment_completed(self, id: int) -> str:
        """Increments the completed missions count
            of the agent with a matching id."""
        stmt = """
        UPDATE `agents`
        SET
        `completed_missions` = `completed_missions` + 1
        WHERE `id` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            return f"Successfully update completed missions for agent {id}."

    def increment_failed(self, id: int) -> str:
        """Increments the failed missions count
            of the agent with a matching id."""
        stmt = """
        UPDATE `agents`
        SET
        `failed_missions` = `failed_missions` + 1
        WHERE `id` = %s;
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            return f"Successfully update failed missions for agent {id}."
        
    def get_agent_performance(self, id: int) -> dict[str, int]:
        """
        Calculates and returns  a summary of the agents performance. 
        Returns a dictionary of the folowing structure:
        {
            "total":0, the total amount of missions assigned to this agent.
            "failed":0, the total amount of missions this agent failed to complete.
            "completed":0, the total amount of missions completed by this agent.
            "success_rate":0 the success rate for this agent.
        }
        Note that an agent with no missions at all has a 0 success rate!
        """
        stmt = """
        with j AS (
            SELECT 
                missions.id AS `m_id`,
                agents.id as `a_id`,
                agents.completed_missions,
                agents.failed_missions
            FROM `agents`
            RIGHT JOIN `missions` ON
                missions.assigned_agent_id  = agents.id)
            Select
            COUNT(*) AS `total`,
            `completed_missions` as `completed`,
            `failed_missions` AS `failed`
            FROM `j`
            GROUP BY `a_id`
            HAVING `a_id` = %s
            LIMIT 1;
        """
        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt, (id,))
            result = cur.fetchone() or {}
        result["failed"] = result.get("failed", 0)
        result["total"] = result.get("total", 0)
        result["completed"] = result.get("completed", 0)
        if result["total"] > 0:
            result["success_rate"] = (100 / result["total"]) * result["completed"]
        else:
            result["success_rate"] = 0
        return result

    def count_active_agents(self) -> int:
        """Returns a count of all existing agents."""
        stmt = """
        SELECT COUNT(`is_active`) AS `active_agents`
        FROM `agents`
        GROUP BY `is_active`
        HAVING `is_active` = TRUE
        """

        with self.db_con(dictionary = True) as cur:
            cur.execute(stmt)
            return cur.fetchone()["active_agents"]
