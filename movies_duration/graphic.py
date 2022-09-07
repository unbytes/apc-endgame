import pandas as pd
import plotly.express as px
from utils.functions import get_column

PATH_MCU_BOX_OFFICE = 'assets\data\mcu_box_office.csv'

mcu_movie_info_dataframe = pd.read_csv(PATH_MCU_BOX_OFFICE)

spider_duration = 0                                                             # Inicialização dos tempos de cada franquia em 0
iron_duration = 0
thor_duration = 0
captain_duration = 0
avengers_duration = 0
guardian_duration = 0
ant_duration = 0

only_movie_names = list()
only_movie_duration = list()

movie_duration_column = get_column(mcu_movie_info_dataframe, 'movie_duration') 
movie_title_column = get_column(mcu_movie_info_dataframe, 'movie_title')

for index, movie_name in enumerate(movie_title_column):                         # Percorre os filmes para agrupa-los por franquia
      if movie_name[:4] == 'Spid':
          spider_duration += movie_duration_column[index]                       # Exemplo de agrupamento dos filmes da franquia (Spider-Man)
      elif movie_name[:4] == 'Iron':
          iron_duration += movie_duration_column[index]
      elif movie_name[:4] == "Thor":
          thor_duration += movie_duration_column[index]
      elif movie_name[:15] == "Captain America":
          captain_duration += movie_duration_column[index]
      elif movie_name[:4] == "Aven" or movie_name[:7] == "The Ave":
          avengers_duration += movie_duration_column[index]
      elif movie_name[:4] == "Guar":
          guardian_duration += movie_duration_column[index]
      elif movie_name[:3] == 'Ant':
          ant_duration += movie_duration_column[index]
      else:
          only_movie_names.append(movie_name)                                   # Adiciona um filme isolado de uma franquia
          movie_duration = movie_duration_column[index]
          only_movie_duration.append(movie_duration)                            # Adiciona a duração do filme isolado
    
movies_name = ["Spider Movies", "Iron Man Movies",
               "Thor Movies","Captain America Movies",
               "Avengers Movies", "Guardians of the Galaxy Movies",
               "Ant-man Movies", *only_movie_names]
movies_duration = [spider_duration, iron_duration,
                  thor_duration, captain_duration,
                  avengers_duration, guardian_duration,
                  ant_duration, *only_movie_duration]

mcu_movies_duration_graphic = px.pie(names=movies_name, values=movies_duration, color_discrete_sequence=px.colors.sequential.Emrld)
mcu_movies_duration_graphic.update_layout(title_text='Representatividade de cada franquia (min)', template='plotly_dark')
