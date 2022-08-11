import pandas as pd
dados = pd.read_csv("mcu_box_office.csv")
value_duration = 0
for data in dados.movie_duration:
    value_duration += data
movie_porcent = [ ]
for duration in dados.movie_duration:
    porcent = (100*duration)/value_duration
    movie_porcent.append(porcent)
movie_names = [ ]
for name in dados.movie_title:
    movie_names.append(name)
    
print(movie_names)
print(movie_porcent)    
print(value_duration)
dados["movie_duration"].value_counts()