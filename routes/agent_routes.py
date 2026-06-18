from fastapi import APIRouter, status, HTTPException
from models import AgentCreateModel, HTTPResponseModel
from services import AgentService


router = APIRouter()


agent_service = AgentService()


@router.post('',
             status_code=status.HTTP_201_CREATED,
             response_model=HTTPResponseModel)
def create_agent(data: AgentCreateModel):
    result = agent_service.create_agent(data=data)
    message = 'success creating agent.'
    return HTTPResponseModel(message=message, data=result)

@router.get('',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_all_agents():
    result = agent_service.get_all_agents()
    message = 'success fetching all agents.'
    return HTTPResponseModel(message=message, data=result)
    
@router.get('/{id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_agent_by_id(id: int):
    result = agent_service.get_agent_by_id(id=id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    message = 'success fetching agent.'

    return HTTPResponseModel(message=message, data=result)

@router.put('/{id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def update_agent(id: int, data: AgentCreateModel):
    result = agent_service.update_agent(id=id, data=data)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    message = 'success fetching agent.'

    return HTTPResponseModel(message=message, data=result)

@router.put('/{id}/deactivate',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def deactivate_agent(id: int):
    result = agent_service.deactivate_agent(id=id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    message = 'success deactivating agent.'

    return HTTPResponseModel(message=message, data=result)

@router.get('/{id}/performance',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_agent_performance(id: int):
    result = agent_service.get_agent_performance(id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    message = 'success fetching agent\'s performance.'

    return HTTPResponseModel(message=message, data=result)
