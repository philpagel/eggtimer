DOCKER = podman

build:
	$(DOCKER) compose build

down:
	$(DOCKER) compose down

up:
	$(DOCKER) compose up -d

refresh: down build up

.PHONEY: build down up refresh
