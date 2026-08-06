from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():
    return {
        "message": "Welcome to AI Learning Agent"
    }