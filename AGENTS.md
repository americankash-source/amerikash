# AmeriKash Codex Instructions

## Project goal
Build AmeriKash as a FastAPI-based financial agent backend. Start as a clean modular monolith and keep boundaries clear so agents can later become microservices.

## Development commands
- Install dependencies: `pip install -r requirements.txt`
- Run app: `uvicorn app.main:app --reload`
- Run tests: `pytest -q`

## Coding standards
- Keep files small and focused.
- Prefer deterministic, testable financial logic before adding LLM calls.
- Do not hardcode secrets or API keys.
- Add or update tests for every behavior change.
- Financial outputs must include disclaimers where user-facing recommendations are generated.
