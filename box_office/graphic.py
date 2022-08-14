import pandas as pd
from math import isnan

PATH_ASIA_PACIFIC = 'assets/data/asia_pacific_box_office.csv'
PATH_EUROPE = 'assets/data/europe_box_office.csv'
PATH_MIDDLE_EAST_AND_AFRICA = 'assets/data/middle_east_and_africa_box_office.csv'
PATH_NORTH_AMERICA = 'assets/data/north_america_box_office.csv'
PATH_SOUTH_AMERICA = 'assets/data/south_america_box_office.csv'

asia_pacific_box_office = pd.read_csv(PATH_ASIA_PACIFIC)
europe_box_office = pd.read_csv(PATH_EUROPE)
middle_east_and_africa_box_office = pd.read_csv(PATH_MIDDLE_EAST_AND_AFRICA)
north_america_box_office = pd.read_csv(PATH_NORTH_AMERICA)
south_america_box_office = pd.read_csv(PATH_SOUTH_AMERICA)

dataframes = [asia_pacific_box_office, europe_box_office, middle_east_and_africa_box_office, north_america_box_office, south_america_box_office]

MOVIES_NUMBER = 27

def sum_continent_box_office(dataframe, column_title):
    continent_box_office  = list()
    for line in range(MOVIES_NUMBER):
        box_office = 0
        for country in dataframe.keys():
            if not country == column_title:
                if not isnan(dataframe[country][line]):
                    box_office += dataframe[country][line]
                else:
                    box_office += 0
        continent_box_office.append(box_office)
    return continent_box_office

continent_box_office = list()
for continent in dataframes:
    continent_box_office.append(sum_continent_box_office(continent, 'movie_title'))

movies_box_office = list()
for movie_index in range(MOVIES_NUMBER):
    movie_box_office = 0
    for continent in continent_box_office:
        movie_box_office += continent[movie_index]
    movies_box_office.append(movie_box_office)

print(movies_box_office)
