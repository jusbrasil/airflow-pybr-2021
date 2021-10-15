# Apache Airflow - Python Brasil 2021

Este tutorial apresenta vários exemplos práticos de como construir DAGs no Apache Airflow.

## Background

Apache Airflow é uma das principais ferramentas de orquestração de workflows, onde você define as tarefas como Directed Acyclic Graphs (DAGs). 
O Airflow permite que você construa pipelines de dados escrevendo apenas códigos Python. 
Quando os workflows são definidos como código, eles se tornam manuteníveis, versionáveis, testáveis e colaborativos.

<img src="https://airflow.apache.org/docs/apache-airflow/stable/_images/arch-diag-basic.png">

## Rodando localmente

Para rodar localmente é necessário, você atender aos seguintes **pré-requisitos**:

- Instalar o Docker Community Edition (CE) na sua máquina. É recomendável que sua máquina tenha ao menos 4GB de RAM livres.
- Instalar o Docker Compose v1.29.1 ou alguma versão mais nova na sua máquina.

Para **iniciar o ambiente**, basta executar o comando abaixo:

`make start-airflow`

Para **limpar o ambiente**, basta executar o seguinte comando:

`make reset-airflow`