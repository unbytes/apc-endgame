import pandas as pd
import plotly.graph_objects as go
#importar o arquivo
dados = pd.read_csv("mcu_box_office.csv")
#variável de 100% do gráfico
value_duration = 0
#somando todos os minutos
for data in dados.movie_duration:
    value_duration += data
#variável de cada porcentagem por filme 
movie_porcent = [ ]
#cálculo de porcentagem 
for duration in dados.movie_duration:
    porcent = (100*duration)/value_duration
    movie_porcent.append(porcent)
#guardar os nomes dos filmes em um vetor
movie_names = [ ]
for name in dados.movie_title:
    movie_names.append(name)

#gráfico
fig = go.Figure(data=[go.Pie(labels=movie_names, values=movie_porcent)])