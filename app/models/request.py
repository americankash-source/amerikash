from pydantic import BaseModel, Field


class FinancialRequest(BaseModel):
    user_id: str = Field(..., min_length=1)
    income: float = Field(..., ge=0)
    expenses: float = Field(..., ge=0)
    goals: list[str] = Field(default_factory=list)
