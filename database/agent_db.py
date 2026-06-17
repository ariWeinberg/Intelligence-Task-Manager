from database.db_connection import DBConnection
from models.agent_create_model import AgentCreateModel
from models.agent_update_model import AgentUpdateModel


class AgentDB:
    def __init__(self, connection_manager: DBConnection):
        pass

    def create_agent(self, data: AgentCreateModel):
        pass

    def get_all_agents(self):
        pass

    def get_agent_by_id(self, id: int):
        pass

    def update_agent(self, id: int, data: AgentUpdateModel):
        pass

    def deactivate_agent(self, id: int):
        pass

    def increment_completed(self, id: int):
        pass

    def increment_failed(self, id: int):
        pass

    def get_agent_performance(self, id: int):
        pass

    def count_active_agents(self):
        pass
