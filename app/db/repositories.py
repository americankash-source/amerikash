from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import create_auth_token, hash_password, verify_password
from app.db.models import AuthToken, FinancialPlanRecord, User
from app.models.auth import LoginRequest, RegisterRequest
from app.models.request import FinancialRequest


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.execute(select(User).where(User.email == email.lower())).scalar_one_or_none()


def create_user(db: Session, request: RegisterRequest) -> User:
    user = User(email=request.email.lower(), password_hash=hash_password(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, request: LoginRequest) -> User | None:
    user = get_user_by_email(db, request.email)
    if not user or not verify_password(request.password, user.password_hash):
        return None
    return user


def create_user_token(db: Session, user: User) -> AuthToken:
    token = AuthToken(user_id=user.id, token=create_auth_token())
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


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


def list_financial_plans(db: Session, user_id: str | None = None, limit: int = 20) -> list[FinancialPlanRecord]:
    query = select(FinancialPlanRecord).order_by(FinancialPlanRecord.created_at.desc()).limit(limit)
    if user_id:
        query = (
            select(FinancialPlanRecord)
            .where(FinancialPlanRecord.user_id == user_id)
            .order_by(FinancialPlanRecord.created_at.desc())
            .limit(limit)
        )
    return list(db.execute(query).scalars().all())


def get_financial_plan(db: Session, plan_id: int) -> FinancialPlanRecord | None:
    return db.get(FinancialPlanRecord, plan_id)
