from typing import Literal
from pydantic import BaseModel, Field, model_validator


class AgentViewModel(BaseModel):
    agent_name: str | None = Field(
            alias="name",
            max_length=50)
    agent_specialty: str | None = Field(
            alias="specialty",
            max_length=50)
    agent_agent_rank: Literal[
            'Junior',
            'Senior',
            'Commander'
            ] | None = Field(
            alias="agent_rank")

    @model_validator
    def validator(self):
        if any((
            self.agent_name,
            self.agent_specialty,
            self.agent_agent_rank
            )):
            return self
        raise ValueError("at least one field must be set to update an agent.")