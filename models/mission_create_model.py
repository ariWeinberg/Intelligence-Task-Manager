from typing import Literal
from pydantic import BaseModel, Field
from models.types import MissionRiskLevel, MissionStatus


class MissionCreateModel(BaseModel):
    mission_title: str = Field(alias="title", max_length=50)
    mission_description: str = Field(alias="description")
    mission_location: str = Field(alias="location", max_length=50)
    mission_difficulty: int = Field(alias="difficulty", ge=1, le=10)
    mission_importance: int = Field(alias="importance", ge=1, le=10)
    mission_status: MissionStatus = Field(alias="status", default='NEW')
    mission_assigned_agent_id: int | None = Field(alias="assigned_agent_id", default=None)

    def risk_level(self) -> MissionRiskLevel:
        level = self.mission_difficulty * 2 + self.mission_importance

        if level < 10:
            return 'LOW'

        if level < 18:
            return 'MEDIUM'

        if level < 25:
            return 'HIGH'

        return 'CRITICAL'
