from fastapi import APIRouter, status
from models import AgentCreateModel, HTTPResponseModel

router = APIRouter()

@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=HTTPResponseModel)
def create_agent(data: AgentCreateModel):
    pass

@router.get('/',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_all_agents():
    pass
    
@router.get('/{agent_id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_agent_by_id(agent_id: int):
    pass

@router.put('/{agent_id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def update_agent(agent_id: int, data: AgentCreateModel):
    pass

@router.put('/{agent_id}/deactivate',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def deactivate_agent(agent_id: int):
    pass

@router.get('/{agent_id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_agent_performance(agent_id: int):
    pass
