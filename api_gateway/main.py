from fastapi import FastAPI

from automobile_service.api import router as automobile_router
from part_service.api import router as part_router
from file_service.api import router as file_router
from discovery_service.api import router as discovery_router

app = FastAPI()


app.include_router(discovery_router, prefix="/discovery")
app.include_router(automobile_router, prefix="/automobile")
app.include_router(part_router, prefix="/part")
app.include_router(file_router, prefix="/file")
