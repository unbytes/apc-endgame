import pandas as pd

from utils.functions import get_column_without_nan, unique_value_list

from datetime import datetime

PATH_MARVEL_COMICS_DATASET = 'https://raw.githubusercontent.com/MateusVrs/apc-endgame/PePa/04/assets/data/Marvel_Comics.csv'
mcu_comics_dataframe = pd.read_csv(PATH_MARVEL_COMICS_DATASET)

YEARS_COLUMN_TITLE = "publish_date"
RATING_COLUMN_TITLE = 'Rating'

publish_date = get_column_without_nan(mcu_comics_dataframe, YEARS_COLUMN_TITLE)
rating_column = get_column_without_nan(mcu_comics_dataframe, RATING_COLUMN_TITLE)
unique_rating = unique_value_list(rating_column)

# Listas das décadas

ninety = list()
ten = list()
twenty = list()

# Listas das contagens

count90 = list()
count10 = list()
count20 = list()
rating_counts = list()

# Função para retirar as strings Nones de listas

def filter_none(column):
    not_none_values = list()
    for value in column:
        if value != 'None':
            not_none_values.append(value)
    return not_none_values


# Extrai os anos de publicação do quadrinhos
publish_years = list()

for date in publish_date:
    try:
        time = datetime.strptime(date, "%B %d, %Y")
        publish_years.append(time.year)
    except:
        publish_years.append(0)

# Laço de repetição usado para colocar cada classificação indicativa em sua respectiva década

for rating, year in zip(rating_column, publish_years):
    if year >= 1990 and year <= 1999:
        ninety.append(rating)
    elif year >= 2000 and year <= 2009:
        ten.append(rating)
    elif year >= 2010 and year <= 2019:
        twenty.append(rating)

# Listas com as etiquetas de décadas que vão ser usadas no gráfico

label90 = list()
label10 = list()
label20 = list()
rating_labels = list()

# 4 laços para criar e adcionar as contagens e as etiquetas RELEVANTES de cada quadrinho em suas épocas

MINIMUM_COUNT = 10
unique_rating_without_none = filter_none(unique_rating)

for rating in unique_rating_without_none:
    count = ninety.count(rating)
    if count >= MINIMUM_COUNT:
        count90.append(count)
        label90.append(rating)

for rating in unique_rating_without_none:
    count = ten.count(rating)
    if count >= MINIMUM_COUNT:
        count10.append(count)
        label10.append(rating)

for rating in unique_rating_without_none:
    count = twenty.count(rating)
    if count >= MINIMUM_COUNT:
        count20.append(count)
        label20.append(rating)

for rating in unique_rating_without_none:
    count = rating_column.count(rating)
    if count >= 500:
        rating_labels.append(rating)
        rating_counts.append(count)
