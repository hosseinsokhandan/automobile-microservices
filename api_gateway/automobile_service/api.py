from fastapi import APIRouter

router = APIRouter()


@router.get("{id}")
async def get(id: int):
    pass
