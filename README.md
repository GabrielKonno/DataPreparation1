# Data Preparation na Prática
Este projeto foi desenvolvido como parte de um exercício de prática e treinamento em Data Preparation. O código realiza uma série de operações de preparação de dados, como limpeza, transformação e junção de dados, simulando um processo comum em projetos de análise de dados. Abaixo, estão descritas as etapas e objetivos principais do código.

## Funcionalidades
O script realiza as seguintes operações principais:

## Importação de Dados:

Carrega datasets de arquivos CSV para realizar as transformações de preparação de dados.
Utiliza bibliotecas pandas e numpy para manipulação de dados.
Limpeza e Transformação de Dados:

Remoção de colunas desnecessárias, como Unnamed: 0, name, category, goal, pledged, e usd pledged para reduzir a dimensionalidade e focar em dados relevantes.
Padronização da coluna usd_goal_real, removendo caracteres não numéricos.
Conversão de dados temporais, usando expressões regulares para remover informações de horário da coluna launched e formatando as colunas launched e deadline para o tipo datetime.
Criação de Novas Variáveis:

Cálculo de uma nova variável time_range, que representa o tempo de campanha em dias entre launched e deadline.
Manipulação de Outras Tabelas:

Carregamento e limpeza de outro dataset (campaign.csv), com remoção de colunas irrelevantes, como Text Description.
Realização de merge entre os datasets principais (DataPrepFinal.csv e campaign.csv), unindo-os com base na coluna ID.
Carregamento de um terceiro dataset (invested.csv) e aplicação de técnicas de codificação dummy na coluna backedLocation, permitindo uma análise mais granular de dados categóricos.
Agrupamento dos dados do dataset invested.csv para calcular a média da idade (age) e somar variáveis dummy de localização (backedLocation_BR, backedLocation_GBK, backedLocation_US), organizando as informações por ID.
Realização de um segundo merge, integrando os dados de invested.csv com o dataset principal, com base em ID.

## Pré-requisitos
Python 3.x
Bibliotecas pandas e numpy
Arquivos CSV: DataPrepFinal.csv, campaign.csv, e invested.csv

## Como Usar
Clone este repositório e carregue os arquivos DataPrepFinal.csv, campaign.csv, e invested.csv no mesmo diretório do script.
Execute o script em um ambiente Python, como Jupyter Notebook, Google Colab, ou diretamente em uma IDE de sua preferência.
Analise os resultados das etapas de preparação e transformação, verificando os dados transformados e prontos para análise.

## Observações
Este script foi criado para fins educacionais e de prática, oferecendo uma visão prática sobre o preparo de dados para análise, com um pipeline simples de manipulação e integração de datasets.
