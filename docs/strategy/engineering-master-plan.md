# AmeriKash Engineering Master Plan

## Engineering Vision
Build AmeriKash as a modular, testable, secure financial agent platform that starts as a clean monolith and can evolve into microservices without rewriting core business logic.

## Current Architecture

```text
FastAPI App
├── API routes
├── Agent layer
├── Service layer
├── DB models/repositories
└── Tests
```

## Architecture Principles
1. Keep business logic deterministic and testable.
2. Avoid duplicate routes, models, agents, and service abstractions.
3. Keep HTTP routes thin.
4. Keep persistence behind repository functions.
5. Keep financial logic inside agents.
6. Keep infrastructure behavior in services/core/db.
7. Add tests before or alongside behavior changes.

## Service Boundary Roadmap

### Current: Modular Monolith
All modules run in one FastAPI app.

### Next: Service-Ready Modules
Define boundaries for:
- Orchestrator
- Cashflow
- Risk
- Investment
- Audit
- User/Auth
- Analytics

### Later: Microservices
Extract services only when there is a real scaling, ownership, or deployment need.

## Sprint 1 Engineering Priorities
1. Stabilize DB layer.
2. Add health checks and persistence tests.
3. Add Alembic migrations.
4. Add user model and authentication.
5. Add plan history endpoints.

## Database Strategy

### Current
SQLite-compatible development with SQLAlchemy.

### Near-Term
PostgreSQL-ready config through Docker/container runtime when available.

### Production Direction
- PostgreSQL for transactional data
- Alembic for migrations
- Redis for background jobs/cache
- Object storage for exported reports if needed
- Analytics warehouse later

## Testing Strategy

### Required Test Types
- API smoke tests
- Agent unit tests
- DB persistence tests
- Auth/security tests
- Regression tests for bugs

### Test Command
```bash
python -m pytest -q
```

## Deployment Roadmap

### Phase 1
Local Python runtime + SQLite fallback.

### Phase 2
Containerized API + PostgreSQL.

### Phase 3
Cloud deployment on Render, Railway, Fly.io, AWS ECS, or similar.

### Phase 4
CI/CD with staging/prod environments.

## Observability Roadmap
- Structured logging
- Request IDs
- Audit event tracking
- Metrics endpoint
- Error monitoring
- Distributed tracing after microservices

## Security Roadmap
- Environment-based secrets
- Password hashing
- JWT auth
- Role-based access later
- Rate limiting
- Data encryption at rest where supported
- Strict audit logs

## Engineering Guardrails
Do not move to microservices too early. The correct path is:

```text
Clean monolith → clear boundaries → service extraction only when necessary
```

## Near-Term Technical Debt To Address
- Wrap financial plan and audit write in a single transaction.
- Add Alembic migration environment.
- Add DB persistence tests.
- Replace `on_event` startup with lifespan handler later if desired.
- Introduce domain-specific error handling.
