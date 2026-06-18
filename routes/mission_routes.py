from tarfile import data_filter

from fastapi import APIRouter, status, HTTPException
from models import AgentCreateModel, HTTPResponseModel
from models.mission_create_model import MissionCreateModel
from services import AgentService
from services.mission_service import MissionService


router = APIRouter()


mission_service = MissionService()


@router.post('',
             status_code=status.HTTP_201_CREATED,
             response_model=HTTPResponseModel)
def create_mission(data: MissionCreateModel):
    result = mission_service.create_mission(data=data)
    message = 'success creating mission.'
    return HTTPResponseModel(message=message, data=result)

@router.get('',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_all_missions():
    result = mission_service.get_all_missions()
    message = 'success fetching all missions.'
    return HTTPResponseModel(message=message, data=result)

@router.get('/{id}',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def get_mission_by_id(id: int):
    result = mission_service.get_mission_by_id(id=id)
    message = 'success fetching mission.'
    return HTTPResponseModel(message=message, data=result)

# @router.put('/{id}/assign/{agent_id}',
#              status_code=status.HTTP_200_OK,
#              response_model=HTTPResponseModel)
# def assign_mission_to_agent(id: int, agent_id: int):
#     result = mission_service.assign_mission(m_id=id, a_id=agent_id)
#     message = 'success assigning mission.'
#     return HTTPResponseModel(message=message, data=result)


@router.put('/{id}/start',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def start_mission(id: int):
    result = mission_service.start_mission(id=id)

@router.put('/{id}/complete',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def complete_mission(id: int):
    result = mission_service.complete_mission(id=id)

@router.put('/{id}/fail',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def fail_mission(id: int):
    result = mission_service.fail_mission(id=id)

@router.put('/{id}/cancel',
             status_code=status.HTTP_200_OK,
             response_model=HTTPResponseModel)
def cancel_mission(id: int):
    result = mission_service.cancel_mission(id=id)