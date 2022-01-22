from typing import List, Optional
from pydantic import BaseModel


class RedisServiceInstanceSchema(BaseModel):
    port: str
    host: str


class RedisServiceSchema(BaseModel):
    name: str
    instances: List[RedisServiceInstanceSchema] = []


class ServiceInSchema(BaseModel):
    name: str
