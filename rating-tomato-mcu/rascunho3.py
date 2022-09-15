from dash import Dash, html, dcc, Input, Output
import pandas as pd 
import plotly.express as px

# leitura dos dados
mcu_movies_df = pd.read_csv('assets/data/movie_info.csv')

def get_column(dataframe, column):
    matrix = dataframe.values.tolist() #Lista de lista, por isso e um matriz
    #funcao do python que transforma o dataframe em lista
    title_position = list(dataframe).index(column)
    column_list = list()
    for values in matrix:
        column_list.append(values[title_position])
    return column_list

# criação de variaveis para a separação das fases
production_budget = get_column(mcu_movies_df, 'production_budget_in_million_(USD)')
movie_name  = get_column(mcu_movies_df, 'movie_title')
phase_one = production_budget[:6]
phase_two = production_budget[6:12]
phase_three = production_budget[12:23]
phase_four = production_budget[23:]

phase_one_movies = movie_name[:6]
phase_two_movies = movie_name[6:12]
phase_three_movies = movie_name[12:23]
phase_four_movies = movie_name[23:]

# custos dos filmes separados por fases
def list_sum(values):
  summation = 0
  for value in values:
    summation += value
  return summation

TO_BILLION = 1000                                                               
count_phase_one = list_sum(phase_one)/TO_BILLION                                
count_phase_two = list_sum(phase_two)/TO_BILLION
count_phase_three = list_sum(phase_three)/TO_BILLION
count_phase_four = list_sum(phase_four)/TO_BILLION

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children ='Fases do UCM'),
    html.H2(children = 'Gráfico com os custos de cada filme, em sua respectiva fase.'),
    html.Div(children='''
        Interação referente as fases do UCM e seus respectivos filmes.
    '''),
    dcc.Dropdown(['Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Todas as Fases'], 'Todas as Fases', id='fases_ucm'),
    dcc.Graph(
        id ='grafico_interação',
    )
])

@app.callback(
    Output('grafico_interação', 'figure'),
    Input('fases_ucm', 'value')
)
def update_output(value):
    if value == "Todas as Fases":
        fig = px.bar(x=["Fase 1", "Fase 2", "Fase 3", "Fase 4"], y=[count_phase_one, count_phase_two, 
        count_phase_three, count_phase_four],
        title=('Custos do UCM por Fases'), labels={'x': 'Fases do UCM', 'y': 'Custo em Bilhão'})
        fig.update_traces(marker_color='#a408c7')
        fig.update_layout(template='plotly_dark')
    elif value == "Fase 1":
         fig = px.bar(x = phase_one_movies, y = phase_one, labels={'x': 'Filmes', 'y': 'Custo em Milhão'})
         fig.update_traces(marker_color='#a408c7')
         fig.update_layout(template='plotly_dark')
    elif value == "Fase 2":
         fig = px.bar(x = phase_two_movies, y = phase_two, labels={'x': 'Filmes', 'y': 'Custo em Milhão'})
         fig.update_traces(marker_color='#a408c7')
         fig.update_layout(template='plotly_dark')
    elif value == "Fase 3":
         fig = px.bar(x = phase_three_movies, y = phase_three, labels={'x': 'Filmes', 'y': 'Custo em Milhão'})
         fig.update_traces(marker_color='#a408c7')
         fig.update_layout(template='plotly_dark')
    elif value == "Fase 4":
         fig = px.bar(x = phase_four_movies, y = phase_four, labels={'x': 'Filmes', 'y': 'Custo em Milhão'})
         fig.update_traces(marker_color='#a408c7')
         fig.update_layout(template='plotly_dark')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)