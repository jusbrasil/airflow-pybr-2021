# inicia o Postgres
start-db:
	@docker-compose up -d postgres
	@docker-compose up initdb

# inicia o Airflow
start-airflow: start-db
	@docker-compose up webserver scheduler

# para o Airflow
stop-airflow:
	@docker-compose down

# Limpa o Airflow, os volumes do Docker e os containers
reset-airflow:
	@docker-compose down -v || true
	@docker-compose rm -f
	rm -f webserver_config.py

# Faz o rebuild de todas as imagens docker
rebuild-airflow:
	@docker-compose build
