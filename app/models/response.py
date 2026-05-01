from pydantic import BaseModel


class CashflowResult(BaseModel):
    income: float
    expenses: float
    surplus: float
    savings_rate: float
    status: str


class RiskResult(BaseModel):
    risk_score: float
    level: str


class InvestmentResult(BaseModel):
    monthly_investment: float
    allocation: dict[str, float]
    disclaimer: str


class FinancialPlanResponse(BaseModel):
    cashflow: CashflowResult
    risk: RiskResult
    investment: InvestmentResult
