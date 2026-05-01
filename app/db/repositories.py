from sqlalchemy.orm import Session

from app.db.models import FinancialPlanRecord
from app.models.request import FinancialRequest


def save_financial_plan(db: Session, request: FinancialRequest, result: dict) -> FinancialPlanRecord:
    record = FinancialPlanRecord(
        user_id=request.user_id,
        income=request.income,
        expenses=request.expenses,
        result=result,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
