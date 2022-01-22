from typing import Optional
from fastapi import APIRouter, HTTPException, Request
from discovery_service.core import registery_service
from discovery_service.models import ServiceInSchema
from discovery_service.schemas import RedisServiceSchema

router = APIRouter()


@router.post("/")
def register_service(service: ServiceInSchema, request: Request):
    registery_service.insert(service, request)
    return {"detail": "OK"}


@router.get("/", response_model=RedisServiceSchema)
def get_service(service: str, request: Request):
    x = registery_service.lookup(service)
    if not x:
        raise HTTPException(status_code=404)
    print(request)
    print(request.client.port)
    print(dir(request))
    return x
