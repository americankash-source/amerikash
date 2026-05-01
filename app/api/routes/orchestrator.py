from fastapi import APIRouter

from app.agents.orchestrator import OrchestratorAgent
from app.models.request import FinancialRequest
from app.models.response import FinancialPlanResponse

router = APIRouter()


@router.post("/", response_model=FinancialPlanResponse)
def run_plan(request: FinancialRequest) -> dict:
    return OrchestratorAgent().run(request)
