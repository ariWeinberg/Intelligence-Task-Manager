from database import AgentDB
from models.agent_create_model import AgentCreateModel
from models.agent_view_model import AgentViewModel


class AgentService:
    def __init__(self, db_layer: AgentDB | None = None):
        self.db_layer = db_layer or AgentDB()

    def create_agent(self, data: AgentCreateModel) -> AgentViewModel:
        return self.db_layer.create_agent(data=data)

    def get_all_agents(self) -> list[AgentViewModel]:
        return self.db_layer.get_all_agents()

    def get_agent_by_id(self, id: int) -> AgentViewModel | None:
        return self.db_layer.get_agent_by_id(id=id)

    def update_agent(self, id: int, data: AgentCreateModel) -> str | None:
        agent = self.db_layer.get_agent_by_id(id=id)
        if agent is None:
            return None
        return self.db_layer.update_agent(id=id, data=data)

    def deactivate_agent(self, id: int) -> str | None:
        if self.db_layer.get_agent_by_id(id=id) is None:
            return None

        return self.db_layer.deactivate_agent(id=id)

    def increment_completed(self, id: int) -> str | None:
        if self.db_layer.get_agent_by_id(id=id) is None:
            return None

        return self.db_layer.increment_completed(id=id)

    def increment_failed(self, id: int) -> str | None:
        if self.db_layer.get_agent_by_id(id=id) is None:
            return None

        return self.db_layer.increment_failed(id=id)

    def get_agent_performance(self, id: int) -> dict[str, int] | None:
        if self.db_layer.get_agent_by_id(id=id) is None:
            return None

        return self.db_layer.get_agent_performance(id=id)

    def count_active_agents(self) -> int:
        return self.db_layer.count_active_agents()
