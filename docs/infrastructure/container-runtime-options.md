# Container Runtime Options for AmeriKash

If Docker Desktop is blocked or unavailable, consider these alternatives.

## Podman Desktop (Recommended First Alternative)
- Docker-compatible workflow for many use cases.
- Can install desktop app per-user on Windows.
- Still requires WSL2/virtualization for Windows container runtime.

## Rancher Desktop
- Full local container runtime with Kubernetes support.
- Good for more advanced infra workflows.
- Requires WSL/virtualization on Windows.

## Deferred Containerization Strategy
If local container tooling is blocked:
1. Continue development using SQLite/local Python runtime.
2. Defer container-based infra until environment constraints are resolved.
3. Keep architecture container-ready in repo.

## AmeriKash Recommendation
Use local Python/SQLite for core feature development until container runtime is available.
Only require container infra for:
- PostgreSQL/Redis/Kafka local parity
- Deployment simulation
- Multi-service orchestration
