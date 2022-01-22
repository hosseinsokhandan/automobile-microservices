from fastapi import FastAPI

from api_gateway.automobile_service.api import router as automobile_router
from api_gateway.part_service.api import router as part_router
from api_gateway.file_service.api import router as file_router
from api_gateway.discovery_service.api import router as discovery_router

app = FastAPI()


app.include_router(discovery_router, prefix="/discovery")
app.include_router(automobile_router, prefix="/automobile")
app.include_router(part_router, prefix="/part")
app.include_router(file_router, prefix="/file")
