up:
	docker compose up

down:
	docker compose down -v

logs:
	docker compose logs api --follow

dependencies:
	uv export --format requirements-txt > requirements.txt

test:
	uv run pytest
