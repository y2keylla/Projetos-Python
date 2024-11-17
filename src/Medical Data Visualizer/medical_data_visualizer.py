import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 1
df = pd.read_csv('medical_examination.csv')

# 2 Calcular o IMC e adicionar a coluna 'overweight'
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3 Normalizar as variáveis colesterol e gluc
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5 Criar o DataFrame para o gráfico categórico
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # 6 Agrupar os dados por "cardio" e contar os valores de cada característica
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

    # 7 Criar o gráfico categórico
    fig = sns.catplot(data=df_cat, kind="bar", x="variable", hue="value", col="cardio", 
                      hue_order=[0, 1], height=5, aspect=1.2)
    fig.set_axis_labels("Feature", "Count")
    fig.set_titles("Cardio = {col_name}")

    # 8 Acessar as barras no gráfico para o teste
    for ax in fig.axes.flat:
        bars = [rect for rect in ax.patches if isinstance(rect, mpl.patches.Rectangle)]
        print(len(bars))  # Aqui você pode verificar o número de barras

    # 9 Salvar o gráfico em um arquivo
    fig.savefig('catplot.png')
    return fig


# 10 Função para o gráfico de correlação Heat Map
def draw_heat_map():
    # 11 Limpar os dados para o gráfico 
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])]  # Pressão diastólica <= pressão sistólica
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]  # Filtrar altura abaixo do 2.5º percentil
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]  # Filtrar altura acima do 97.5º percentil
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]  # Filtrar peso abaixo do 2.5º percentil
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]  # Filtrar peso acima do 97.5º percentil

    # 12 
    corr = df_heat.drop(columns=['BMI']).corr()  # Remover a coluna 'BMI'

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, cmap='coolwarm', cbar_kws={'shrink': 0.8}, annot_kws={"size": 10})

    # 16 Salvar o gráfico
    fig.savefig('heatmap.png')
    return fig
