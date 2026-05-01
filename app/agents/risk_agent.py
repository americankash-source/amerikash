from app.agents.base import BaseAgent


class RiskAgent(BaseAgent):
    def run(self, data: dict) -> dict:
        income = max(float(data.get("income", 0)), 1.0)
        expenses = float(data.get("expenses", 0))
        risk_score = min(1.0, max(0.0, expenses / income))
        level = "high" if risk_score > 0.7 else "medium" if risk_score > 0.4 else "low"
        return {"risk_score": round(risk_score, 4), "level": level}
