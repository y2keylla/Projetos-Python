# Projetos-Python

Este repositório contém cinco projetos desenvolvidos em Python que abrangem diversas áreas como análise de dados, visualização, estatísticas e predições. Cada projeto está organizado em sua própria pasta com o código e os dados necessários.

## Estrutura do Repositório

```
root/
│
├── mean-variance-calculator/
│   └── mean_var_std.py
│
├── demographic-data-analyzer/
│   ├── demographic_data_analyzer.py
│   └── demographic_data.csv
│
├── medical-data-visualizer/
│   ├── medical_data_visualizer.py
│   └── medical_examination.csv
│
├── time-series-visualizer/
│   ├── time_series_visualizer.py
│   └── fcc-forum-pageviews.csv
│
├── sea-level-predictor/
│   ├── sea_level_predictor.py
│   └── epa-sea-level.csv
│
└── README.md
```


## Descrição dos Projetos

### 1. Mean-Variance-Standard Deviation Calculator
Este projeto implementa uma função `calculate()` que aceita uma lista de 9 números e retorna cálculos estatísticos básicos (média, variância, desvio padrão, etc.) organizados em um dicionário.

### 2. Demographic Data Analyzer
Usando Pandas, este projeto analisa dados demográficos extraídos do banco de dados Census de 1994. Ele responde a perguntas como:
- Quantas pessoas de cada raça estão representadas no conjunto de dados?
- Qual a média de idade dos homens?
- Qual porcentagem de pessoas com educação avançada ganha mais de 50K, entre outros.

### 3. Medical Data Visualizer
Este projeto utiliza Pandas, Matplotlib e Seaborn para visualizar dados médicos e identificar relações entre doenças cardíacas, medidas corporais, marcadores sanguíneos e estilo de vida. Gera gráficos categóricos e mapas de calor com correlações entre variáveis.

### 4. Time Series Visualizer
Analisa dados de séries temporais do fórum do freeCodeCamp, criando gráficos para:
- Visualizar padrões de visitas diárias (linha).
- Médias mensais agrupadas por ano (barras).
- Tendências sazonais e anuais (box plot).

### 5. Sea Level Predictor
Analisa mudanças no nível do mar desde 1880, utilizando modelos de regressão linear para prever o aumento do nível do mar até 2050, com gráficos de tendências.