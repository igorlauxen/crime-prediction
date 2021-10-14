# Trabalho de Machine Learning

Neste trabalho esta sendo considerado um subset dos dados de [Crimes in Chicago](https://www.kaggle.com/currie32/crimes-in-chicago).

O objetivo é realizar uma predição de crimes em data área baseado no histórico de crimes que ocorreram.

O algoritmo a ser considerado é [Random Forest](https://en.wikipedia.org/wiki/Random_forest)

## Pre-Requisitos para executar

- [VSCode]()
- [Pycharm]()
- [Python3]()

## TODO list

- [ ] Decidir quais colunas do Excel vão ser consideradas
- [ ] Executar RF com o mínimo possível de dados
  - Colunas mínimas: Primary Type, Latitude, Longitude, todas as colunas de data (após formato)
- [ ] Adicionar ao RF todas as colunas String necessárias
  - Colunas necessárias: Primary Type, Description

## Nice to know

Para splitar os arquivos foi usado o comando:

`split -l 500000 Chicago_Crimes_2012_to_2017.csv generated_file_`

funciona no windows se usar o [cmder](https://cmder.net/)