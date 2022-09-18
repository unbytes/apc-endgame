from dash import Dash, dcc, html, Input, Output
import plotly.express as px

from movies_duration.graphic import movie_title_column, movie_duration_column, movies_duration, movies_name, phases_order, movie_phases

import sys
sys.path.append('./')

app = Dash(__name__)

app.layout = html.Main(children=[
    html.Section(className='column-container', children=[
        html.H1(children='Duração dos filmes da Marvel'),
        html.Div(children=[
            html.Label('Escolha o filtro de representatividade:'),
            dcc.Dropdown(['Filmes', 'Por fases', 'Por Franquia'],
                         value='valor', id='movies-duration-dropdown'),
        ]),
        dcc.Graph(
            id="movies-duration-graph"
        )
    ])
])


@app.callback(
    Output('movies-duration-graph', 'figure'),
    Input('movies-duration-dropdown', 'value')
)
def update_movies_duration_graphic(value):
    if value == 'Por fases':
        graphic_figure = px.pie(names=movie_title_column, values=movie_duration_column,
                                color_discrete_sequence=px.colors.sequential.Emrld)
        title = 'Representatividade de cada fase (min)'
    elif value == 'Por Franquia':
        graphic_figure = px.pie(names=movies_name, values=movies_duration,
                                color_discrete_sequence=px.colors.sequential.Emrld)
        title = 'Representatividade de cada franquia (min)'
    elif value == 'Filmes':
        graphic_figure = px.pie(names=phases_order, values=movie_phases,
                                color_discrete_sequence=px.colors.sequential.Emrld)
        title = 'Representatividade dos filmes (min)'

    graphic_figure.update_layout(title_text=title, template='plotly_dark')

    return graphic_figure


if __name__ == '__main__':
    app.run_server(debug=True)
