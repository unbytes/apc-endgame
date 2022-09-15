import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# leitura dos dados
mcu_movies_df = pd.read_csv('assets/data/movie_info.csv')

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



#receita

#podemos fazer o lucro por fase também

#interação mostrar os filmes de cada fase


earnings = mcu_movies_df['worldwide_box_office']
ganho_one = earnings[[0] + [1] + [2] + [3] + [4] + [5]]
ganho_two = earnings[[6] + [7] + [8] + [9] + [10] + [11]]
ganho_three = earnings[[12] + [13] + [14] + [15] + [16] + [17] + [18] + [19] + [20] + [21] + [22]]
ganho_four = earnings [[23] + [24] + [25] + [26]]

# gráfico a seguir...
fig = px.bar(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], y=[count1, count2, count3, count4],




title=('Custos do UCM por Fases'), labels={'x': 'Fases do UCM', 'y': 'Custo em Bilhão'})
fig.update_traces(marker_color='#a408c7')
fig.update_layout(template='plotly_dark')
fig.show() 



fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], y=[ganho_one, ganho_two, ganho_three, ganho_four], name="yaxis data"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], name="yaxis2 data"),
    secondary_y=True,
)