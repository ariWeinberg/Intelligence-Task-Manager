from typing import Any
from pydantic import BaseModel, Field


class HTTPResponseModel(BaseModel):
    message: str = Field()
    data: Any = Field()
