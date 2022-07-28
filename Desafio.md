# Desafio

Este desafio consiste no desenvolvimento de uma pipeline ETL para extração e manipulação de dados sobre população da California.

## Desenvolvimento:


    - Use as ferramentas e tecnologias de sua escolha - #(Preferencialmente desenvolver em Python)# - e armazene o código no GitHub. 
    - Aproveite este oportunidade para demonstrar suas habilidades em alguma estrutura de orquestração de pipeline de dados e tecnologia de conteinerização!
    - Além disso, lembre-se de adicionar etapas ao pipeline para verificar se os dados extraídos são consistentes com os valores consolidados nas tabelas raw.
    

**O arquivo de origem está disponível na raiz do projeto ou pelo link [aqui](https://github.com/dadosmaistodos/challenge-data-engineering/blob/main/california_housing_train.csv).** 

#
# Objetivo     
    
# 1 - Exploração:


1.1 - Qual a coluna com maior desvio padrão?
#

1.2 - Qual valor mínimo e o máximo?


#
## 2 - Trabalhando com colunas:


2.1 - Criar coluna hma_cat, baseada na coluna housing_median_age, conforme as regras abaixo:

    *  Se < 18 então de_0_ate_18.
    *  Se >= 18 E < 29 entao ate_29.
    *  Se >= 29 E < 37 entao ate_37.
    *  Se >= 37 então acima_37.    
#
2.2 - Criar a coluna c_ns:

    * Onde longitude abaixo (<) de -119 recebe o valor norte e acima(>=) sul. 
#

2.3 - Renomer as colunas:

    * hma_cat > age
    * c_ns > california_region

### Escrevendo o resultado localmente em parquet, armazenar os dados no seguinte formato:


| Coluna              | Datatype    |
| --------------------| ----------- |
| `age`               | `string`    |
| `california_region` | `string`    |
| `total_rooms`       | `double`    |
| `total_bedrooms`    | `double`    |
| `population`        | `double`    |
| `households`        | `double`    |
| `median_house_value`| `double`    |

#
## 3 - Agregações:

3.1 - Escreva um arquivo no formato Parquet localmente considerando o dataframe final, crie a seguinte analise:

    * Age
    * California_region
    * S_population: Soma de population
    * M_median_house_value: Média de median_house_value

Ordenado decrescente por median_house_value

#

| Coluna                | Datatype    |
| ----------------------| ----------- |
| `age`                 | `string`    |
| `california_region`   | `string`    |
| `s_population`        | `double`    |
| `m_median_house_value`| `double`    |


*Bom Desafio!*

