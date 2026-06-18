from typing import Literal
from pydantic import BaseModel, Field


class AgentViewModel(BaseModel):
    agent_id: int = Field(alias="id", gt=0)
    agent_name: str = Field(alias="name", max_length=50)
    agent_specialty: str = Field(alias="specialty", max_length=50)
    agent_is_active: bool = Field(alias="is_active", default=True)
    agent_completed_missions: int = Field(alias="completed_missions", default=0)
    agent_failed_missions: int = Field(alias="failed_missions", default=0)
    agent_agent_rank: Literal['Junior', 'Senior', 'Commander'] = Field(alias="agent_rank")
