from app.agents.base import BaseAgent

DISCLAIMER = "Educational planning output only. This is not financial, legal, or tax advice."


class InvestmentAgent(BaseAgent):
    def run(self, cashflow: dict, risk: dict) -> dict:
        surplus = max(float(cashflow.get("surplus", 0)), 0.0)
        risk_score = float(risk.get("risk_score", 0.5))
        if surplus <= 0:
            allocation = {"stocks": 0.0, "bonds": 0.0, "cash": 1.0}
        elif risk_score > 0.7:
            allocation = {"stocks": 0.4, "bonds": 0.4, "cash": 0.2}
        elif risk_score > 0.4:
            allocation = {"stocks": 0.6, "bonds": 0.3, "cash": 0.1}
        else:
            allocation = {"stocks": 0.7, "bonds": 0.2, "cash": 0.1}
        return {
            "monthly_investment": surplus,
            "allocation": allocation,
            "disclaimer": DISCLAIMER,
        }
