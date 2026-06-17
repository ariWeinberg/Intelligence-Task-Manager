from database.db_connection import DBConnection
from models.agent_create_model import AgentCreateModel
from models.agent_update_model import AgentUpdateModel
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
        `name` = %s,
        `specialty` = %s,
        `agent_rank` = %s;
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
            return cur.fetchone() or None

    def update_agent(self, id: int, data: AgentUpdateModel) -> str:
        """Applys the update data to the agent with a matching id."""
        pass

    def deactivate_agent(self, id: int) -> str:
        """Deactivates an agent."""
        pass

    def increment_completed(self, id: int) -> str:
        """Increments the completed missions count
            of the agent with a matching id."""
        pass

    def increment_failed(self, id: int) -> str:
        """Increments the failed missions count
            of the agent with a matching id."""
        pass

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
        """
        pass

    def count_active_agents(self) -> int:
        """Returns a count of all existing agents."""
        pass
