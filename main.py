from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from mysql.connector import DatabaseError, ProgrammingError
import uvicorn
from models.HTTP_response_model import HTTPResponseModel
from routes.agent_routes import router as agent_router
from routes.mission_routes import router as mission_router


app = FastAPI()


app.include_router(agent_router, prefix="/agents")
app.include_router(mission_router, prefix="/missions")


def route_exception_handller(r: Request, e: Exception):
    message=""
    data={
        "error_message": str(e),
        "error_type": str(type(e)),
        }
    headers = None
    status_code = 200

    if isinstance(e, HTTPException):
        message = str(e)
        status_code=e.status_code
        headers=e.headers

    elif isinstance(e, DatabaseError):
        message = "database error occourd."
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR    

    else:
        message = "Unknown Error."
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse(
        content={
            'message': message,
            'data': data
        },
        headers=headers,
        status_code=status_code
    )


app.add_exception_handler(Exception, route_exception_handller)


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8989, reload=True)