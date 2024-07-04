from fastapi import APIRouter

from src.api.v1.views import user_auth_views

# Add route with prefix /api/v1 to manage v1 APIs.
router = APIRouter(prefix="/api/v1")


router.include_router(user_auth_views.router, tags=["App User Endpoints"])
