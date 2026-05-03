from fastapi import APIRouter

from app.api.routes import auth, health, orchestrator, plans, users

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(orchestrator.router, prefix="/plan", tags=["planning"])
api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
