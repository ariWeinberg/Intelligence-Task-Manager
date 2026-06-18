from database import AgentDB
from models.agent_create_model import AgentCreateModel
from models.agent_view_model import AgentViewModel


class AgentService:
    def __init__(self, db_layer: AgentDB | None = None):
        self.db_layer = db_layer or AgentDB()

    def create_agent(self, data: AgentCreateModel) -> AgentViewModel:
        pass

    def get_all_agents(self) -> list[AgentViewModel]:
        pass

    def get_agent_by_id(self, id: int) -> AgentViewModel | None:
        pass

    def update_agent(self, id: int, data: AgentCreateModel) -> str:
        pass

    def deactivate_agent(self, id: int) -> str:
        pass

    def increment_completed(self, id: int) -> str:
        pass

    def increment_failed(self, id: int) -> str:
        pass

    def get_agent_performance(self, id: int) -> dict[str, int]:
        pass

    def count_active_agents(self) -> int:
        pass
