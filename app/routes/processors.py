from app.globals import transaction
from fastapi import APIRouter

router = APIRouter(
    prefix="/processors",
)


@router.get("/")
async def get_processors():
    data = transaction("select id, description, details from processor",
                       fetchall=True)
    return {
        "data": [dict(zip(['id', 'description', 'details'], item))
                 for item in data]}


@router.get("/{processor_id}")
async def get_processor(processor_id: str):
    data = transaction("select id, description, details from processor where id = %s",
                       [processor_id],
                       fetchall=False)
    return dict(zip(['id', 'description', 'details'], data)) if data else {"detail": "Invalid processor id"}
