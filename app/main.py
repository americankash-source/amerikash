from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.models import AuditEvent, FinancialPlanRecord
from app.db.session import Base, engine

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    Base.metadata.create_all(bind=engine, tables=[FinancialPlanRecord.__table__, AuditEvent.__table__])
    yield


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "AmeriKash running"}
