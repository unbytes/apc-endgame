import pandas as pd 
import plotly.express as px
from utils import get_column

# leitura dos dados
mcu_movies_df = pd.read_csv('assets/data/movie_info.csv')

# criação de variaveis para a separação das fases
production_budget = get_column(mcu_movies_df, 'production_budget_in_million_(USD)')
phase_one = production_budget[:6]
phase_two = production_budget[6:12]
phase_three = production_budget[12:23]
phase_four = production_budget[23:]




# custos dos filmes separados por fases
count_phase_one=sum(phase_one)
count_phase_two=sum(phase_two)
count_phase_three=sum(phase_three)
count_phase_four=sum(phase_four)




# custos dos filmes separados por fases


# gráfico a seguir...
fig = px.bar(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], y=[count_phase_one, count_phase_two, count_phase_three, count_phase_four],
title=('Custos do UCM por Fases'), labels={'x': 'Fases do UCM', 'y': 'Custo em Bilhão'})
fig.update_traces(marker_color='#a408c7')
fig.update_layout(template='plotly_dark')
fig.show() 