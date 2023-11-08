# Apresentação

Este projeto implementa o pipeline ETL como requisitado no enunciado do [Desafio](https://github.com/MaisTodos/challenge-data-engineering/blob/main/Desafio.md).

## Instalação e Execução

1. Clone o [repositório](https://github.com/victorvalentee/challenge-data-engineering) em sua máquina local.
    ```bash
    git clone https://github.com/victorvalentee/challenge-data-engineering.git
    ```
2. Instale as dependências necessárias:
    - [Docker](https://docs.docker.com/engine/install/)
    - [bash](https://www.gnu.org/software/bash/)

3. Execute o script `run_project.sh`.
    ```bash
    cd challenge-data-engineering
    sh run_project.sh
    ```

4. Depois que a ETL rodar completamente, você pode excluir os containers criados.
    ```bash
    docker compose down
    ```

5. Os dois arquivos parquet gerados por essa ETL podem ser encontrados em:
- [challenge-data-engineering/etl/output/categorical](./etl/output/categorical)
- [challenge-data-engineering/etl/output/final](./etl/output/final)


## Fonte de dados
A fonte de dados deste projeto é um arquivo `.csv` que contém o *dataset* 'California Housing' (informações residenciais/populacionais da Califórnia). 


## Etapas do pipeline

### 0. Análise Exploratória

A primeira etapa do desafio é fazer a análise exploratória dos dados ([EDA Notebook](etl/EDA_Notebook.ipynb)) e responder às seguintes perguntas:

1. Qual coluna tem o maior desvio padrão?
    > Resposta: `median_house_value`

2. Qual é o valor mínimo e máximo no conjunto de dados?
    > Resposta: *Considerando que esses valores são relativos à coluna `median_house_value`*:  
    Valor mínimo = `14999`  
    Valor máximo = `500001`


### 1. Manipulação Do Dataset

A próxima etapa do pipeline é manipular as colunas do *dataset* e executar as seguintes tarefas:

1. > Criar uma nova coluna categórica chamada `hma_cat` com base na coluna `housing_median_age`, usando as seguintes regras:  
Se o valor for menor que 18, definir o valor como `de_0_ate_18`.  
Se o valor estiver entre 18 e 29, definir o valor como `ate_29`.  
Se o valor estiver entre 29 e 37, definir o valor como `ate_37`.  
Se o valor for maior ou igual a 37, definir o valor como `acima_37`.

2. > Criar uma nova coluna categórica chamada `c_ns` com base na coluna `longitude`, usando a seguinte regra:  
Se o valor for menor que -119, definir o valor como `norte`.  
Se o valor for maior ou igual a -119, definir o valor como `sul`.  

3. > Renomear a coluna `hma_cat` para `age` e a coluna `c_ns` para `california_region`.

### 2. Armazenar Dataset Intermediário

1. Armazenar os dados resultantes da [etapa 1](#1-manipulação-do-dataset) em um arquivo Parquet com as seguintes colunas e tipos de dados:

    | Coluna              | Datatype    |
    | --------------------| ----------- |
    | `age`               | `string`    |
    | `california_region` | `string`    |
    | `total_rooms`       | `double`    |
    | `total_bedrooms`    | `double`    |
    | `population`        | `double`    |
    | `households`        | `double`    |
    | `median_house_value`| `double`    |


### 3. Transformações Finais (WIP)

A etapa final do pipeline é realizar transformações adicionais nos dados e armazenar o *dataset* resultante em um arquivo Parquet. 

1. Schema do dataframe final:

    | Coluna                | Datatype    | Descrição |
    | ----------------------| ----------- | --------- |
    | `age`                 | `string`    | - |
    | `california_region`   | `string`    | - |
    | `s_population`        | `double`    | Soma da coluna `population` |
    | `m_median_house_value`| `double`    | Média da coluna `median_house_value` |

2. O dataframe final deve ser ordenado de forma decrescente pela coluna `m_median_house_value`.
