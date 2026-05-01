from app.agents.base import BaseAgent


class CashflowAgent(BaseAgent):
    def run(self, data: dict) -> dict:
        income = float(data.get("income", 0))
        expenses = float(data.get("expenses", 0))
        surplus = income - expenses
        savings_rate = surplus / income if income > 0 else 0.0
        status = "positive" if surplus > 0 else "break_even" if surplus == 0 else "negative"
        return {
            "income": income,
            "expenses": expenses,
            "surplus": surplus,
            "savings_rate": round(savings_rate, 4),
            "status": status,
        }
