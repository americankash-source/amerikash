from sqlalchemy.orm import Session

from app.agents.cashflow_agent import CashflowAgent
from app.agents.investment_agent import InvestmentAgent
from app.agents.risk_agent import RiskAgent
from app.db.repositories import save_financial_plan
from app.models.request import FinancialRequest
from app.services.audit_service import AuditService


class OrchestratorAgent:
    def __init__(self, db: Session | None = None, audit_service: AuditService | None = None) -> None:
        self.db = db
        self.cashflow = CashflowAgent()
        self.risk = RiskAgent()
        self.investment = InvestmentAgent()
        self.audit = audit_service or AuditService(db=db)

    def run(self, request: FinancialRequest) -> dict:
        request_data = request.model_dump()
        cashflow_result = self.cashflow.run(request_data)
        risk_result = self.risk.run(request_data)
        investment_result = self.investment.run(cashflow_result, risk_result)
        final = {
            "cashflow": cashflow_result,
            "risk": risk_result,
            "investment": investment_result,
        }
        if self.db:
            save_financial_plan(self.db, request, final)
        self.audit.log("financial_plan_generated", {"user_id": request.user_id, "result": final})
        return final
