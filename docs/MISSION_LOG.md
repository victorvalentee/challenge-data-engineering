# Mission Log

Esse arquivo contém o registro das decisões importantes tomadas durante o desenvolvimento desse projeto.

## Day 1

1. Inicialização do projeto:
    - Fork do projeto no GitHub
    - Primeiro commit: desabilitei o versionamento dos arquivos csv no .gitignore
    - Baixei o docker-compose do Airflow [conforme a documentação](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml)

2. Testar as configurações default do docker-compose e checar funcionamento do PySpark dentro do container.
    - Para baixar a imagem e criar os containers: `docker compose up -d`

    - Aiflow funcionando OK. Para fazer login, usar as credenciais padrão (airflow/airflow)
    ![Alt text](assets/img/image.png)

    - Python instalado corretamente no container "airflow-worker":
        ```docker compose run airflow-worker airflow info```
    ![Alt text](assets/img/image-1.png)

3. Desabilitar versionamento de código dos logs gerados pelos containers.

4. Pyspark não está instalado no container, então decidi adicionar a imagem `jupyter/pyspark-notebook` ao docker compose. Dessa forma poderei testar a ETL interativamente pelo notebook enquanto desenvolvo.