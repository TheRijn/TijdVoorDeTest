DOCKER_EXEC=docker compose exec app
.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: init
init: install up migrate fixtures ## setup the application from scratch

.PHONY: up
up: ## Starts the app
	@docker compose up -d --force-recreate

.PHONY: down
down: ## Stops the app
	@docker compose down --remove-orphans

.PHONY: build
build:  ## (Re)build the containers
	@echo ✨ Building container
	@docker compose build

.PHONY: shell
shell: ## Opens a shell in the app container
	@${DOCKER_EXEC} bash

.PHONY: migrate
migrate: ## Migrate the database to the latest version
	@echo ✨ Appling migrations
	@${DOCKER_EXEC} python manage.py migrate

.PHONY: compilemessages
compilemessages:  ## Compile translations
	@echo ✨ Compiling translations
	@${DOCKER_EXEC} python manage.py compilemessages  --ignore .venv

.PHONY: install
install: ## Install dependencies in container
	@echo ✨ Installing dependencies
	@docker compose run --rm --entrypoint="" app poetry install --without prod --sync

.PHONY: fixtures
fixtures:
	@echo ✨ Loading fixtures
	@${DOCKER_EXEC} python manage.py loaddata krtek

.PHONY: _clean
_clean:
	@echo ✨ Stopping containers
	@docker compose down -v
	@echo ✨ Removing compiled files
	@rm -f tvdt/**/locale/*/LC_MESSAGES/django.mo

.PHONY: clean
clean: _clean init

