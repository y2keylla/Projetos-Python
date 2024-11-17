import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Registrando conversores de data para Matplotlib
register_matplotlib_converters()

# Importar os dados
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Limpar os dados - removendo os 2.5% maiores e menores valores
lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)
df_cleaned = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]


def draw_line_plot():
    # Criando uma cópia dos dados para não modificar o original
    df_copy = df_cleaned.copy()
    
    # Plotando o gráfico de linha
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_copy.index, df_copy['value'], color='b', lw=0.7)
    
    # Adicionando título e rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Salvando a imagem e retornando o gráfico
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copiar e modificar dados para o gráfico de barras mensal
    df_bar = df_cleaned.copy()
    
    # Extraindo ano e mês para o agrupamento
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Calculando a média de visualizações por mês e ano
    monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plotando o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    monthly_avg.plot(kind='bar', ax=ax, stacked=False)

    # Adicionando título e rótulos
    ax.set_title('Average Monthly Page Views by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Page Views')

    # Adicionando legenda
    ax.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Salvando a imagem e retornando o gráfico
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Preparando os dados para os gráficos de caixa
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [int(d.year) for d in df_box.date]  # Convertendo para int explicitamente
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Garantindo que os dados 'value' sejam convertidos para tipo float
    df_box['value'] = df_box['value'].astype(float)

    # Criando a figura para os subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Gráfico de caixa por ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Gráfico de caixa por mês
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Ajustando os meses para começar em janeiro
    axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Salvando a imagem e retornando o gráfico
    fig.savefig('box_plot.png')
    return fig
