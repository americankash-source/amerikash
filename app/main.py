from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.models import AuditEvent, FinancialPlanRecord
from app.db.session import Base, engine

setup_logging()

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(api_router)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine, tables=[FinancialPlanRecord.__table__, AuditEvent.__table__])


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "AmeriKash running"}
