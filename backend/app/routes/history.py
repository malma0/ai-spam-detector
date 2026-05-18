from fastapi import APIRouter, Depends, Query
from app.security import verify_api_key

router = APIRouter()


fake_history = [
    {
        "id": 1,
        "input_text": "Win free iPhone now!",
        "result_text": "SPAM",
        "score": 0.98,
        "created_at": "2026-05-18 12:00:00"
    },
    {
        "id": 2,
        "input_text": "Hello, how are you?",
        "result_text": "NOT SPAM",
        "score": 0.95,
        "created_at": "2026-05-18 12:10:00"
    }
]


@router.get(
    "/history",
    dependencies=[Depends(verify_api_key)]
)
async def get_history(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):

    offset = (page - 1) * limit

    paginated_items = fake_history[offset: offset + limit]

    return {
        "page": page,
        "limit": limit,
        "items": paginated_items
    }