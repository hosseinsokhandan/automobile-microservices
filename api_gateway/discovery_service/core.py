import json
from os import name
from fastapi import Request
from redis import Redis
from api_gateway.discovery_service.schemas import (
    RedisServiceInstanceSchema,
    RedisServiceSchema,
    ServiceInSchema,
)
from api_gateway.settings import get_settings

settings = get_settings()


class ServiceDiscovery:
    def __init__(self) -> None:
        self.storage: Redis = Redis.from_url(settings.DISCOVERY_URL)

    def lookup(self, service_name: str):
        lookup = self.storage.get(service_name)
        if lookup:
            return json.loads(lookup)
        return lookup

    def insert(self, service: ServiceInSchema, request: Request):
        lookup = self.lookup(service.name)
        
        if lookup:
            redis_data = RedisServiceSchema(**lookup)
        else:
            redis_data = redis_data = RedisServiceSchema(name=service.name)

        redis_data.instances.append(
            RedisServiceInstanceSchema(
                host=request.client.host, port=request.client.port
            )
        )
        resp = self.storage.set(service.name, redis_data.json())
        return resp


registery_service = ServiceDiscovery()
