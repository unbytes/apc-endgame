import pandas as pd
import plotly.graph_objects as go

PATH_MCU_BOX_OFFICE = 'assets\data\mcu_box_office.csv'

# Omportar o arquivo
mcu_dataframe = pd.read_csv(PATH_MCU_BOX_OFFICE)

# variáveis dos conjuntos de filmes
spider_duration = 0
iron_duration = 0
thor_duration = 0
captain_duration = 0
avengers_duration = 0
guardian_duration = 0
ant_duration = 0

# Guardar os nomes dos filmes em um vetor
movie_names = list()
for name in mcu_dataframe.movie_title:
    movie_names.append(name)

# Variável de cada porcentagem por filme 
movie_duration = [ ]

# Cálculo de conjuntos dos filmes
for duration in mcu_dataframe.movie_duration:
    movie_duration.append(duration)
cont = 0
#divisao de conjunto de filmes
for name in movie_names:
    
    if name[:4] == 'Spid':
        spider_duration += movie_duration[cont]
    elif name[:4] == 'Iron':
        iron_duration += movie_duration[cont]
    elif name[:4] == "Thor":
        thor_duration += movie_duration[cont]
    elif name[:4] == "Capt":
        captain_duration += movie_duration[cont]
    elif name[:4] == "Aven":
        avengers_duration += movie_duration[cont]
    elif name[:4] == "Guar":
        guardian_duration += movie_duration[cont]
    elif name[:3] == 'Ant':
        ant_duration += movie_duration[cont]
    cont += 1 
x = 0
y = 0
z = 0
u = 0
t = 0
b = 0
a = 0
new_names_movie = list()
new_duration_movie = list()
for name in movie_names:
    if name[:4] == 'Spid' and x != 1:
        name = "Spider Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(spider_duration)
        x = 1
    elif name[:4] == 'Iron' and a != 1:
        name = "Iron Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(iron_duration)
        a = 1
    elif name[:4] == "Thor" and b != 1:
        name = "Thor Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(thor_duration)
        b = 1
    elif name[:4] == "Capt" and t != 1:
        name = "Captain America Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(captain_duration)
        t = 1
    elif name[:4] == "Aven" and u != 1:
        name = "Avengers Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(avengers_duration)
        u = 1
    elif name[:4] == "Guar" and z != 1:
        name = "Guardians of the Galaxy Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(guardian_duration)
        z = 1
    elif name[:3] == 'Ant' and y != 1:
        name = "Ant-man Movies"
        new_names_movie.append(name) 
        new_duration_movie.append(ant_duration)
        y = 1
    else:
        new_names_movie.append(name)
        number = movie_duration[]
        new_duration.append
    


# Gráfico
#fig = go.Figure(data=[go.Pie(labels=mcu_dataframe.movie_title, values=mcu_dataframe.movie_duration)])
#fig.show()
