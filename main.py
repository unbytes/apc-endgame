import sys
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

sys.path.append('./')

from box_office.graphic import box_office_graphic, asia_pacific , europe , middle_east_and_africa , north_america , south_america, asia_pacific_box_office

app = Dash()

app.layout = html.Div(children = [
    html.H1(children = 'Bilheteria dos filmes do MCU'),
    html.H2(children = 'Esse gráfico indica a bilheteria de cada filme do MCU'),
    html.Div(children = 'Obs: O gráfico engloba os filmes do Homem de Ferro 1 até o Homem Aranha: Sem volta para casa'),
    dcc.Dropdown(['Ásia Pacífica', 'Europa', 'Oriente Médio e África', 'América do Norte', 'América do Sul', 'Todas as regiões do planeta'],value = 'Todas as regiões do planeta', id = 'demo-dropdown'),
    dcc.Graph(
        id = 'graphic',
    )
])

@app.callback(
    Output('graphic', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == 'Todas as regiões do planeta':
        fig = box_office_graphic
    elif value == 'Ásia Pacífica':
        fig = px.bar(x=asia_pacific_box_office.movie_title , y = asia_pacific, labels = {'x': 'Filmes do MCU', 'y' : 'Bilheteria em milhão'})
        fig.update_traces(marker_color='#B11313', marker_opacity=0.9)
        fig.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
    elif value == 'Europa':
        fig = px.bar(x=asia_pacific_box_office.movie_title , y = europe , labels = {'x': 'Filmes do MCU', 'y' : 'Bilheteria em milhão'})
        fig.update_traces(marker_color='#B11313', marker_opacity=0.9)
        fig.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
    elif value == 'Oriente Médio e África':
        fig = px.bar(x=asia_pacific_box_office.movie_title , y = middle_east_and_africa , labels = {'x': 'Filmes do MCU', 'y' : 'Bilheteria em milhão'})
        fig.update_traces(marker_color='#B11313', marker_opacity=0.9)
        fig.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
    elif value == 'América do Norte':
        fig = px.bar(x=asia_pacific_box_office.movie_title , y = north_america , labels = {'x': 'Filmes do MCU', 'y' : 'Bilheteria em milhão'})
        fig.update_traces(marker_color='#B11313', marker_opacity=0.9)
        fig.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
    elif value == 'América do Sul':
        fig = px.bar(x=asia_pacific_box_office.movie_title , y = south_america , labels = {'x': 'Filmes do MCU', 'y' : 'Bilheteria em milhão'})
        fig.update_traces(marker_color='#B11313', marker_opacity=0.9)
        fig.update_layout(xaxis_range=[0,27], template= 'plotly_dark')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
