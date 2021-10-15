# inicia o Postgres
setup-airflow:
	mkdir -p ./dags ./logs ./plugins
	echo -e "AIRFLOW_UID=$(id -u)" > .env
	@docker-compose up airflow-init

# inicia o Airflow
start-airflow: setup-airflow
	@docker-compose up -d

# para o Airflow
stop-airflow:
	@docker-compose down --volumes --remove-orphans

# Limpa o Airflow, os volumes do Docker e os containers
reset-airflow:
	@docker-compose down -v || true
	@docker-compose rm -f
	rm -rf .env ./logs ./plugins