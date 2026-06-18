from database.mission_db import MissionDB
from models.agent_view_model import AgentViewModel
from models.mission_create_model import MissionCreateModel
from models.mission_view_model import MissionViewModel
from models.types import MissionStatus


class MissionService:
    def __init__(self, db_layer: MissionDB | None = None):
        self.db_layer = db_layer or MissionDB()

    def create_mission(self, data: MissionCreateModel) -> MissionViewModel:
        pass

    def get_all_missions(self) -> list[MissionViewModel]:
        pass
    
    def get_mission_by_id(self, id: int) -> MissionViewModel:
        pass
    
    def assign_mission(self, m_id: int, a_id: int) -> str:
        pass
    
    def update_mission_status(self, id: int, status: MissionStatus) -> str:
        pass
    
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
