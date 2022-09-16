import pandas as pd
from math import isnan
import plotly.express as px
from utils.functions import get_column

asia_pacific_box_office = pd.read_csv('assets/data/asia_pacific_box_office.csv')
europe_box_office = pd.read_csv('assets/data/europe_box_office.csv')
middle_east_and_africa_box_office = pd.read_csv('assets/data/middle_east_and_africa_box_office.csv')
north_america_box_office = pd.read_csv('assets/data/north_america_box_office.csv')
south_america_box_office = pd.read_csv('assets/data/south_america_box_office.csv')

# Definição da variável de quantidade de filmes
movies_number = 27

# Criação da função analyse que analisa o dataframe
def analyse(dataframe):
    box_office_list  = list()
    for movie in range(movies_number):     # Para cada um dos filmes, a variável box_office recebe 0
        box_office = 0
        for country in dataframe.columns:
            if not country == 'movie_title':      # Ignorando a coluna dos títulos dos filmes para o cálculo
                if not isnan(get_column(dataframe , country) [movie]):     # Quando o valor da bilheteria foi definido para o país, ele é somado na variável da bilheteria total do filme
                    box_office += get_column(dataframe , country) [movie] 
                else:     # Quando o valor não foi registrado é somado o 0 
                    box_office += 0
        box_office_list.append(box_office)   # É adicionado na lista o valor total da bilheteria de cada filme
    return box_office_list

# Cada uma das variáveis recebe a lista final da soma das bilheterias dos filmes do continente determinado
asia_pacific = analyse(asia_pacific_box_office) 
europe = analyse(europe_box_office)
middle_east_and_africa = analyse(middle_east_and_africa_box_office)
north_america = analyse(north_america_box_office)
south_america = analyse(south_america_box_office)

# Soma da bilheteria dos filmes
total_box_office = list()
for movie in range(movies_number):
    total_box_office.append(asia_pacific[movie] + europe[movie] + middle_east_and_africa[movie] + north_america[movie] + south_america[movie])

# Criação do gráfico
box_office_graphic = px.bar(x=asia_pacific_box_office.movie_title , y = total_box_office, labels = {'x': 'Filmes do MCU' , 'y' : 'Bilheteria em milhão'})
box_office_graphic.update_traces(marker_color='#B11313', marker_opacity=0.9)
box_office_graphic.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
