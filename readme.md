# Trabalho de Machine Learning

Neste trabalho esta sendo considerado um subset dos dados de [Crimes in Chicago](https://www.kaggle.com/currie32/crimes-in-chicago).

O objetivo é realizar uma predição de crimes em data área baseado no histórico de crimes que ocorreram.

O algoritmo a ser considerado é [Random Forest](https://en.wikipedia.org/wiki/Random_forest)

Inspirado pesadamente nos tutoriais:

1. [Toward Data Science: random forest in python](https://towardsdatascience.com/random-forest-in-python-24d0893d51c0)

## Pre-Requisitos para executar

- [VSCode](https://code.visualstudio.com/)
  - versão utilizada: 1.60.2
- [Python3](https://www.python.org/downloads/)
  - versão utilizada: Python 3.9.2
- [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
  - versão utilizada: pip 21.0.1
  - install the following libs:
    - `pip3 install folium`
    - `pip3 install geopy`
- Baixar o arquivo `generated_file_aa.csv` do [Google Docs](https://drive.google.com/file/d/10P8EF5IAazl2Tef_Z3Pbs8QfKS4-2E4m/view?usp=sharing) e colocar na pasta `/data`
  - link: https://drive.google.com/file/d/10P8EF5IAazl2Tef_Z3Pbs8QfKS4-2E4m/view?usp=sharing
  - esse arquivo é um subset dos dados de Chicago_Crimes_2012_to_2017.csv

## Execução

- Executar o arquivo `main.py`

_Nota:_ a execução do Random Forest em um mac com 16GB de memória demorou mais de 2hr para processar todos os arquivos.

## Estrutura de classes

- main.py
  - classe principal, importa arquivos, chama a classe de preparação de dados e processa usando random forest
- BooleanFormatter.py, DateFormatter.py, TextFormatter.py
  - fazem processamento e limpeza de tabelas baseadas em seus tipos.
- DataPreparator.py
  - Remove colunas desnecessárias, invoca as classes Formatters.py para processamento dos dados
  - Retorna atributos para serem consumidos pelo random forest e o dataframe limpo
- MapAnalyser.py
  - classe suporte: baseado em um dataframe, cria um arquivo html com os pontos dos crimes
  - utilizado para ter uma ideia geral do mapa e se haveria possíveis outliers
  - como o arquivo gerado tem mais de 200mb, somente foi enviado para o repostório screenshots da análise do mapa que podem ser vistos em `map_screenshots`
- FileCreator.py
  - criar um arquivo html vazio abaixo da pasta `map` que é usado pelo MapAnalyzer.py para salvar os dados

## Estrutura de Pastas

- production_code
  - todas as classes que são usadas
- map
  - usada para salvar o html do mapa
- map_screenhsots
  - análise do mapa html
- executions
  - print das execuções do algoritmo com diferentes linhas (250000, 350000 e todas as linhas)
- data
  - pasta onde o arquivo olhara para consumir os dados

## Nice to know

Para splitar os arquivos foi usado o comando:

`split -l 500000 Chicago_Crimes_2012_to_2017.csv generated_file_`

funciona no windows se usar o [cmder](https://cmder.net/)

## Documentos para inspiração

- [Spark + Random Forest](https://www.silect.is/blog/random-forest-models-in-spark-ml/)
- [Working with Geospatial Data in ML](https://heartbeat.comet.ml/working-with-geospatial-data-in-machine-learning-ad4097c7228d)
