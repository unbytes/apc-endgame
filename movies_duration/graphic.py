import pandas as pd

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

phase_1= 0
phase_2= 0
phase_3= 0
phase_4= 0

only_movie_names = list()
only_movie_duration = list()
only_movie_phases = list()

movie_duration_column = get_column(mcu_movie_info_dataframe, 'movie_duration') 
movie_title_column = get_column(mcu_movie_info_dataframe, 'movie_title')
movie_years_column = get_column(mcu_movie_info_dataframe, "release_date")

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

for index, movie_data in enumerate(movie_years_column):
    movie_data1 = movie_data.split("/")
    movie_data1 = int(movie_data1[2])
    if movie_data1 >= 2008 and movie_data1 <= 2012:
        phase_1 += movie_duration_column[index]
    elif movie_data1 >= 2013 and movie_data1 <= 2015:
        phase_2 += movie_duration_column[index]
    elif movie_data1 >= 2016 and movie_data1 <= 2019:
        phase_3 += movie_duration_column[index]
    elif movie_data1 == 2021:
        phase_4 += movie_duration_column[index]

movies_name = ["Spider Movies", "Iron Man Movies",
               "Thor Movies","Captain America Movies",
               "Avengers Movies", "Guardians of the Galaxy Movies",
               "Ant-man Movies", *only_movie_names]
movies_duration = [spider_duration, iron_duration,
                  thor_duration, captain_duration,
                  avengers_duration, guardian_duration,
                  ant_duration, *only_movie_duration]

phases_order = ["Fase 1", "Fase 2", "Fase 3", "Fase 4"]
movie_phases = [phase_1, phase_2, phase_3, phase_4] 
