from fastapi import APIRouter

from src.api.v1.views import hackathon_views

# Add route with prefix /api/v1 to manage v1 APIs.
router = APIRouter(prefix="/api/v1")


router.include_router(hackathon_views.router, tags=["Hackathon Endpoints"])
