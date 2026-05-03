from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.repositories import get_financial_plan, list_financial_plans
from app.db.session import get_db
from app.models.response import FinancialPlanHistoryItem, FinancialPlanHistoryResponse

router = APIRouter()


def _to_history_item(record) -> FinancialPlanHistoryItem:
    return FinancialPlanHistoryItem(
        id=record.id,
        user_id=record.user_id,
        income=record.income,
        expenses=record.expenses,
        result=record.result,
        created_at=record.created_at,
    )


@router.get("/history", response_model=FinancialPlanHistoryResponse)
def plan_history(
    user_id: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
) -> FinancialPlanHistoryResponse:
    records = list_financial_plans(db=db, user_id=user_id, limit=limit)
    return FinancialPlanHistoryResponse(plans=[_to_history_item(record) for record in records])


@router.get("/{plan_id}", response_model=FinancialPlanHistoryItem)
def plan_detail(plan_id: int, db: Session = Depends(get_db)) -> FinancialPlanHistoryItem:
    record = get_financial_plan(db=db, plan_id=plan_id)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    return _to_history_item(record)
