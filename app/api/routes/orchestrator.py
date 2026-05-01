from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import OrchestratorAgent
from app.db.session import get_db
from app.models.request import FinancialRequest
from app.models.response import FinancialPlanResponse

router = APIRouter()


@router.post("/", response_model=FinancialPlanResponse)
def run_plan(request: FinancialRequest, db: Session = Depends(get_db)) -> dict:
    return OrchestratorAgent(db=db).run(request)
