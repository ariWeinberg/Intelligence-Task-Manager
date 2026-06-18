from typing import Literal
from pydantic import BaseModel, Field


class MissionViewModel(BaseModel):
    mission_id: int = Field(alias="id", gt=0)
    mission_title: str = Field(alias="title", max_length=50)
    mission_description: str = Field(alias="description")
    mission_location: str = Field(alias="location", max_length=50)
    mission_difficulty: int = Field(alias="difficulty", ge=1, le=10)
    mission_importance: int = Field(alias="importance", ge=1, le=10)
    mission_status: Literal['NEW', 'ASSIGNED',
                    'IN_PROGRESS', 'COMPLETED',
                    'FAILED', 'CANCELLED'] = Field(alias="'status", default='NEW')
    mission_risk_level: Literal['LOW', 'MEDIUM',
                        'HIGH', 'CRITICAL'] = Field(alias="'risk_level")
    mission_assigned_agent_id: int | None = Field(alias="assigned_agent_id", default=None)
