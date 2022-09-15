import pandas as pd 
import plotly.express as px

# leitura dos dados
mcu_movies_df = pd.read_csv('assets/data/movie_info.csv')


def get_column(dataframe, column):
    matrix = dataframe.values.tolist() #funcao do python que transforma o dataframe em lista
    title_position = list(dataframe).index(column)
    column_list = list()
    for values in matrix:
        for index, value in enumerate(values):
            if index == title_position:
                column_list.append(value)
    return column_list

# print(get_column(mcu_movies_df, 'movie_title'))

# criação de variaveis para a separação das fases
production_budget = mcu_movies_df['production_budget_in_million_(USD)']
phase_one = production_budget[[0] + [1] + [2] + [3] + [4] + [5]]
phase_two = production_budget[[6] + [7] + [8] + [9] + [10] + [11]]
phase_three = production_budget[[12] + [13] + [14] + [15] + [16] + [17] + [18] + [19] + [20] + [21] + [22]]
phase_four = production_budget [[23] + [24] + [25] + [26]]

# custos dos filmes separados por fases
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for product in phase_one:
    count1 += product
for product in phase_two:
    count2+= product
for product in phase_three:
    count3 += product
for product in phase_four:
    count4 += product

# gráfico a seguir...
fig = px.bar(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], y=[count1, count2, count3, count4],
title=('Custos do UCM por Fases'), labels={'x': 'Fases do UCM', 'y': 'Custo em Bilhão'})
fig.update_traces(marker_color='#a408c7')
fig.update_layout(template='plotly_dark')
fig.show() 