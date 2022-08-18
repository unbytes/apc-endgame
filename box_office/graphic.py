import pandas as pd
from math import isnan
import plotly.express as px
from utils.functions import get_column

asia_pacific_box_office = pd.read_csv('assets/data/asia_pacific_box_office.csv')
europe_box_office = pd.read_csv('assets/data/europe_box_office.csv')
middle_east_and_africa_box_office = pd.read_csv('assets/data/middle_east_and_africa_box_office.csv')
north_america_box_office = pd.read_csv('assets/data/north_america_box_office.csv')
south_america_box_office = pd.read_csv('assets/data/south_america_box_office.csv')

movies_number = 27

def analyse(dataframe):
    box_office_list  = list()
    for line in range(movies_number):
        box_office = 0
        for country in dataframe.columns:
            if not country == 'movie_title':
                if not isnan(get_column(dataframe , country)[line]):
                    box_office += get_column(dataframe , country)[line]
                else:
                    box_office += 0
        box_office_list.append(box_office)
    return box_office_list

asia_pacific = analyse(asia_pacific_box_office)
europe = analyse(europe_box_office)
middle_east_and_africa = analyse(middle_east_and_africa_box_office)
north_america = analyse(north_america_box_office)
south_america = analyse(south_america_box_office)

total_box_office = list()
for movie in range(movies_number):
    total_box_office.append(asia_pacific[movie] + europe[movie] + middle_east_and_africa[movie] + north_america[movie] + south_america[movie])

box_office_graphic = px.bar(x=asia_pacific_box_office.movie_title , y = total_box_office , title = 'Bilheteria dos filmes do MCU' , labels = {'x': 'Filmes do MCU' , 'y' : 'Bilheteria em bilhão'})
box_office_graphic.update_traces(marker_color='#B11313', marker_opacity=0.9)
box_office_graphic.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
