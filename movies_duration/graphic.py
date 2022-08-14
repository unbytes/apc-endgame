import pandas as pd
import plotly.graph_objects as go

PATH_MCU_BOX_OFFICE = 'assets\data\mcu_box_office.csv'

# Omportar o arquivo
mcu_dataframe = pd.read_csv(PATH_MCU_BOX_OFFICE)

# Variável de 100% do gráfico
value_duration = 0

# Somando todos os minutos
for data in mcu_dataframe.movie_duration:
    value_duration += data

# Variável de cada porcentagem por filme 
movie_porcent = list()

# Cálculo de porcentagem 
for duration in mcu_dataframe.movie_duration:
    porcent = (100*duration)/value_duration
    movie_porcent.append(porcent)

# Guardar os nomes dos filmes em um vetor
movie_names = list()
for name in mcu_dataframe.movie_title:
    movie_names.append(name)

# Gráfico
fig = go.Figure(data=[go.Pie(labels=mcu_dataframe.movie_title, values=mcu_dataframe.movie_duration)])
fig.show()
