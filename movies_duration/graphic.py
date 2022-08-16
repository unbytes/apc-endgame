import pandas as pd
import plotly.graph_objects as go
from utils import get_column

PATH_MCU_BOX_OFFICE = 'assets\data\mcu_box_office.csv'

# importar o arquivo
mcu_dataframe = pd.read_csv(PATH_MCU_BOX_OFFICE)

# variáveis dos conjuntos de filmes
spider_duration = 0
iron_duration = 0
thor_duration = 0
captain_duration = 0
avengers_duration = 0
guardian_duration = 0
ant_duration = 0
# Lista para guardar os valores 
list_duration_movie = list()
cont = 0
# Lista para guardar os nomes dos filmes em um vetor
movie_names = list()
#Verificar nome por nome e ir juntando
movie_duration_column = get_column(mcu_dataframe, 'movie_duration')
for name in mcu_dataframe.movie_title:
      if name[:4] == 'Spid':
          spider_duration += movie_duration_column[cont]
      elif name[:4] == 'Iron':
          iron_duration += movie_duration_column[cont]
      elif name[:4] == "Thor":
          thor_duration += movie_duration_column[cont]
      elif name[:15] == "Captain America":
          captain_duration += movie_duration_column[cont]
      elif name[:4] == "Aven" or name[:7] == "The Ave":
          avengers_duration += movie_duration_column[cont]
      elif name[:4] == "Guar":
          guardian_duration += movie_duration_column[cont]
      elif name[:3] == 'Ant':
          ant_duration += movie_duration_column[cont]
      else:
          movie_names.append(name)
          list_duration_movie.append(mcu_dataframe.movie_duration[cont])

      cont += 1 
#vetor com os novos nomes dos conjuntos de filme e vetor para os valores de duração     
new_names = ["Spider Movies", "Iron Man Movies",  "Thor Movies", "Captain America Movies", "Avengers Movies", "Guardians of the Galaxy Movies", "Ant-man Movies"]
new_values_duration = [spider_duration, iron_duration, thor_duration, captain_duration, avengers_duration, guardian_duration, ant_duration]
#colocar esses valores nas listas
for name in new_names:
    movie_names.append(name)
for value in new_values_duration:
    list_duration_movie.append(value)

# Gráfico
fig = go.Figure(data=[go.Pie(labels = movie_names, values = list_duration_movie)])
fig.show()
