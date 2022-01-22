from fastapi import APIRouter

router = APIRouter()


@router.get("{automobile_id}")
def list_automobile_parts():
    pass