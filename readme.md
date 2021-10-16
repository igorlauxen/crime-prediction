# Trabalho de Machine Learning

Neste trabalho esta sendo considerado um subset dos dados de [Crimes in Chicago](https://www.kaggle.com/currie32/crimes-in-chicago).

O objetivo é realizar uma predição de crimes em data área baseado no histórico de crimes que ocorreram.

O algoritmo a ser considerado é [Random Forest](https://en.wikipedia.org/wiki/Random_forest)

Inspirado pesadamente nos tutoriais:

1. [Toward Data Science: random forest in python](https://towardsdatascience.com/random-forest-in-python-24d0893d51c0)

## Pre-Requisitos para executar

- [VSCode]()
- [Pycharm]()
- [Python3]()
- [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
  - install the following libs:
    - `pip3 install folium`
    - `pip3 install geopy`

## TODO list

- [X] Decidir quais colunas do Excel vão ser consideradas
- [ ] Executar RF com o mínimo possível de dados
  - [X] Colunas mínimas: Primary Type, Latitude, Longitude, todas as colunas de data (após formato)
- [X] Tem que converter campos booleans para numéricos
- [ ] Adicionar ao RF todas as colunas String necessárias
  - Colunas necessárias: Primary Type, Description, Location
- [ ] Criar/Valuda uma coluna coluna para medir a distancia dos pontos passa saber se já aconteceu um crime perto
- [ ] Necessário revisar as datas para transformar em seno e cosseno talvez?
  - Baseado em [Feature Engineering Cyclical Features](http://blog.davidkaleko.com/feature-engineering-cyclical-features.html)

## Nice to know

Para splitar os arquivos foi usado o comando:

`split -l 500000 Chicago_Crimes_2012_to_2017.csv generated_file_`

funciona no windows se usar o [cmder](https://cmder.net/)

## Documentos para inspiração

- [Spark + Random Forest](https://www.silect.is/blog/random-forest-models-in-spark-ml/)
- [Working with Geospatial Data in ML](https://heartbeat.comet.ml/working-with-geospatial-data-in-machine-learning-ad4097c7228d)
