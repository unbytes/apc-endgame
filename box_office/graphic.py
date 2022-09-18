import pandas as pd
import plotly.express as px
from utils.functions import get_rows_without_nan

asia_pacific_box_office = pd.read_csv(
    'assets/data/asia_pacific_box_office.csv')
europe_box_office = pd.read_csv('assets/data/europe_box_office.csv')
middle_east_and_africa_box_office = pd.read_csv(
    'assets/data/middle_east_and_africa_box_office.csv')
north_america_box_office = pd.read_csv(
    'assets/data/north_america_box_office.csv')
south_america_box_office = pd.read_csv(
    'assets/data/south_america_box_office.csv')

MOVIES_NUMBER = 27


def join_countries_box_office_per_movie(dataframe):
    """Agrupa as bilheterias das partes do mundo para cada filme

    Args:
      dataframe: DataFrame que será usado para extrair as informações

    Return:
      Lista com as bilheterias de cada filme para o respectivo DataFrame
    """
    movies_box_office = list()
    movies_rows = get_rows_without_nan(dataframe)
    for movie_row in movies_rows:
        # Retira o 1º elemento, ou seja, o nome do filme
        region_box_office = movie_row[1:]

        # Soma as bilheterias do respectivo filme em uma região do mundo
        movie_region_box_office = sum(region_box_office)
        movies_box_office.append(movie_region_box_office)
    return movies_box_office


# Agrupa a bilheteria dos países de uma região do mundo para cada filme
asia_pacific = join_countries_box_office_per_movie(asia_pacific_box_office)
europe = join_countries_box_office_per_movie(europe_box_office)
middle_east_and_africa = join_countries_box_office_per_movie(
    middle_east_and_africa_box_office)
north_america = join_countries_box_office_per_movie(north_america_box_office)
south_america = join_countries_box_office_per_movie(south_america_box_office)

# Soma da bilheteria dos filmes
total_box_office = list()
for movie in range(MOVIES_NUMBER):
    total_box_office.append(asia_pacific[movie] + europe[movie] +
                            middle_east_and_africa[movie] + north_america[movie] + south_america[movie])

# Criação do gráfico
box_office_graphic = px.bar(x=asia_pacific_box_office.movie_title, y=total_box_office, labels={
                            'x': 'Filmes do MCU', 'y': 'Bilheteria em milhão'})
box_office_graphic.update_traces(marker_color='#B11313', marker_opacity=0.9)
box_office_graphic.update_layout(template='plotly_dark')
