# Apache Airflow - Python Brasil 2021

Este tutorial apresenta vários exemplos práticos de como construir DAGs no Apache Airflow.

## Background

Apache Airflow é uma das principais ferramentas de orquestração de workflows, onde você define as tarefas como Directed Acyclic Graphs (DAGs). 
O Airflow permite que você construa pipelines de dados escrevendo apenas códigos Python. 
Quando os workflows são definidos como código, eles se tornam manuteníveis, versionáveis, testáveis e colaborativos.

<img src="https://airflow.apache.org/docs/apache-airflow/stable/_images/arch-diag-basic.png">

## Rodando localmente com Pyenv
Você vai precisar de um ambiente virtual com python 3.6+ (recomendamos o 3.9).

### Pyenv
Caso não tenha instalado na maquina, você pode usar o pyenv para ter multiplas versoes do python e criar seu ambiente virtual com ele.
Siga a documentação oficial para instalar o pyenv na sua máquina:
- https://github.com/pyenv/pyenv
- https://github.com/pyenv/pyenv-virtualenv
- https://realpython.com/intro-to-pyenv/

Instale o Pyhton 3.9:

```shell
$ pip install 3.9.7
```

```shell
$ pyenv virtualenv 3.9.7 pybr-airflow
```

```shell
$ pyenv local pybr-airflow
```

**Caso você não tenha o pip instalado**, instale ele na sua máquina seguindo o tutorial abaixo:
- https://pip.pypa.io/en/stable/installation/

### Instalando o Airflow
Depois do ambiente virtual instalado, você vai precisar do `apache-airflow` e do `apache-airflow-providers-docker instalados`. Você pode fazer assim:

```shell
$ pip install apache-airflow apache-airflow-providers-docker
```

Depois você precisa configurar o airflow; para isso siga estes passos:

```shell
$ airflow db init
$ airflow users create --username=admin --firstname test --lastname test --role Admin --email test@test.com
```

Agora você pode rodar o airflow; para isso execute o seguinte comando:

```shell
$ airflow webserver -p 8081
```

Agora acesse a seguinte URL: **http://localhost:8081**.


#### Troubleshooting: Airflow não sendo reconhecido

Caso o comando do airflow não tiver sendo reconhecido, verifique se o `~/.local/bin` na sua variável de ambiente `PATH` está configurada corretamente:

``
PATH=$PATH:~/.local/bin
``

Você também pode iniciar o Airflow com:

```shell
$ python -m airflow
```


## Rodando localmente com Docker Compose

Para rodar localmente é necessário, você atender aos seguintes **pré-requisitos**:

- Instalar o Docker Community Edition (CE) na sua máquina. É recomendável que sua máquina tenha ao menos 4GB de RAM livres.
- Instalar o Docker Compose v1.29.1 ou alguma versão mais nova na sua máquina.

Para **iniciar o ambiente**, basta executar o comando abaixo:

`make start-airflow`

Para **limpar o ambiente**, basta executar o seguinte comando:

`make reset-airflow`
