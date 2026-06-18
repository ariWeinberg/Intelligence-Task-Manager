from database.agent_db import AgentDB
from database.mission_db import MissionDB
from errors import AgentNotFoundError, MissionNotFoundError, NotAllowedError
from models.agent_view_model import AgentViewModel
from models.mission_create_model import MissionCreateModel
from models.mission_view_model import MissionViewModel
from models.types import MissionStatus


class MissionService:
    def __init__(self, mission_db_layer: MissionDB | None = None, agent_db_layer: AgentDB | None = None):
        self.mission_db_layer = mission_db_layer or MissionDB()
        self.agent_db_layer = agent_db_layer or AgentDB()

    def create_mission(self, data: MissionCreateModel) -> MissionViewModel:
        return self.mission_db_layer.create_mission(data=data)

    def get_all_missions(self) -> list[MissionViewModel]:
        return self.mission_db_layer.get_all_missions()
    
    def get_mission_by_id(self, id: int) -> MissionViewModel | None:
        return self.mission_db_layer.get_mission_by_id(id=id)
    
    def assign_mission(self, m_id: int, a_id: int) -> str | None:
        mission = self.mission_db_layer.get_mission_by_id(id=m_id)
        if mission is None:
            raise MissionNotFoundError(m_id=m_id)
        
        agent = self.agent_db_layer.get_agent_by_id(id=a_id)
        if agent is None:
            raise AgentNotFoundError(a_id=a_id)
        
        if agent.agent_agent_rank != 'Commander' and mission.mission_risk_level == 'CRITICAL':
            raise NotAllowedError()


        return self.assign_mission(m_id=m_id, a_id=a_id)
    
    def update_mission_status(self, id: int, status: MissionStatus) -> str | None:
        mission = self.mission_db_layer.get_mission_by_id(id=id)
        if mission is None:
            raise MissionNotFoundError(m_id=id)
        
        return self.mission_db_layer.update_mission_status(id=id, status=status)
    
    def get_open_missions_by_agent(self, id: int) -> list[MissionViewModel]:
        pass
    
    def count_all_missions(self) -> int:
        pass
    
    def count_by_status(self,
                        status: MissionStatus
                        ) -> int:
        pass
    
    def count_open_missions(self) -> int:
        pass
    
    def count_critical_missions(self) -> int:
        pass
    
    def get_top_agent(self) -> AgentViewModel:
        pass

    def start_mission(id: int) -> str | None:
        pass

    def complete_mission(id: int) -> str | None:
        pass

    def fail_mission(id: int) -> str | None:
        pass

    def cancel_mission(id: int) -> str | None:
        pass
