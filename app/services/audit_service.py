from sqlalchemy.orm import Session

from app.db.models import AuditEvent


class AuditService:
    def __init__(self, db: Session | None = None) -> None:
        self.db = db

    def log(self, event_name: str, data: dict) -> None:
        if not self.db:
            return None

        self.db.add(AuditEvent(event_name=event_name, payload=data))
        self.db.commit()
