# Chamar as bibliotecas (Pandas e Plotly)
import pandas as pd
import plotly.graph_objects as go

# Caminho para os dados
PATH_MARVEL_COMICS = 'assets\data\Marvel_Comics.csv'

# Leitura dos dados
comics_dataframe = pd.read_csv(PATH_MARVEL_COMICS)

# Filtrar uma coluna especifica (Rating)
RATING_COLUMN_TITLE = 'Rating'

# Listagem de cada faixa etária
comics_rating = list()
for rating in comics_dataframe[RATING_COLUMN_TITLE]: # Especificando um tipo de dado no data frame (Rating)
    if rating not in comics_rating: # Condicional para verificar se ele está dentro da lista
        comics_rating.append(rating) # Adiciona +1 dado 'Rating' na lista 

# Listagem da frequência de cada faixa etária
rating_count = list()
for rating in comics_rating: # Percorre a lista de faixa etária na lista criada anteriormente
    rating_count.append(list(comics_dataframe[RATING_COLUMN_TITLE]).count(rating)) # Contando quantas vezes cada faixa etária aparece

# Plotagem do gráfico
graphic = go.Figure([go.Pie(labels=comics_rating, values=rating_count)])
graphic.update_layout(title_text='Porcetagem das classificatórias dos quadrinhos da Marvel')
graphic.show()
