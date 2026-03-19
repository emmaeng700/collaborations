from fastapi import APIRouter

router = APIRouter(prefix="/history", tags=["History"])

# TODO (Akontoke): GET /history/{user_id}
# - Query Firestore for all past diagnoses by user
# - Return list sorted by timestamp desc

@router.get("/{user_id}")
async def get_history(user_id: str):
    return {"user_id": user_id, "scans": []}
