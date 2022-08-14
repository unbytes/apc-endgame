import pandas as pd
import plotly.graph_objects as go

PATH_MARVEL_COMICS = 'assets\data\Marvel_Comics.csv'

comics_dataframe = pd.read_csv(PATH_MARVEL_COMICS)

RATING_COLUMN_TITLE = 'Rating'

comics_rating = list()
for rating in comics_dataframe[RATING_COLUMN_TITLE]:
    if rating not in comics_rating:
        comics_rating.append(rating)

rating_count = list()
for rating in comics_rating:
    rating_count.append(list(comics_dataframe[RATING_COLUMN_TITLE]).count(rating))

graphic = go.Figure([go.Pie(labels=comics_rating, values=rating_count)])
graphic.update_layout(title_text='Porcetagem das classificatórias dos quadrinhos da Marvel')
graphic.show()
