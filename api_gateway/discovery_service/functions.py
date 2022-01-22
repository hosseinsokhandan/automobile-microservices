from api_gateway.discovery_service.core import registery_service


def get_service_address(service_name: str):
    return registery_service.lookup(service_name)
