from typing import Literal
from pydantic import BaseModel, Field


class AgentViewModel(BaseModel):
        agent_name: str = Field(alias="name", max_length=50)
        agent_specialty: str = Field(alias="specialty", max_length=50)
        agent_agent_rank: Literal['Junior', 'Senior', 'Commander'] = Field(alias="agent_rank")
