dev:
	python -m uvicorn app.main:app --reload

test:
	python -m pytest -q

docker-up:
	docker compose -f docker/docker-compose.yml up --build
