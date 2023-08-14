runserver-docker:
	@echo "Run docker"
	uvicorn todo-app.app:app --host 0.0.0.0 --port 80 --reload

docker-build:
	docker build -t fastapi-image .

docker-run:
	docker-compose up -d

docker-down:
	docker-compose down
