from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go

from mcu_comics.graphic import count90, label90, count10, label10, count20, label20, rating_counts, rating_labels
from dc_mcu.graphic import dc_wikia_dataframe, mcu_wikia_dataframe

from utils.functions import get_column, unique_value_list

import sys
sys.path.append('./')

app = Dash(__name__)

app.layout = html.Main(children=[
    html.Section(id='characters-characteristics', className='column-container', children=[
        html.H1('Características dos personagens (Marvel e DC)'),
        html.Div(className='column-container', children=[
            html.H2('Cor do cabelo'),
            html.Div(className='row-container', children=[
                html.Label('Escolha o intervalo (Anos):'),
                dcc.RangeSlider(min=1935, max=2013, marks=None, step=1, value=[1935, 2013],
                                id='HAIR-year', className='year-slider',
                                tooltip={"placement": "bottom", "always_visible": True})
            ]),
            dcc.Graph(
                id='HAIR-graph'
            )
        ]),
        html.Div(className='column-container', children=[
            html.H1('Cor dos olhos'),
            html.Div(className='row-container', children=[
                html.Label('Escolha o intervalo (Anos):'),
                dcc.RangeSlider(min=1935, max=2013, marks=None, step=1, value=[1935, 2013],
                                id='EYE-year', className='year-slider',
                                tooltip={"placement": "bottom", "always_visible": True})
            ]),
            dcc.Graph(
                id='EYE-graph'
            )
        ])
    ]),
    html.Section(id="comics-rating", className='column-container', children=[
        html.H1(children='Classificação Etária das HQs'),
        html.Div(className='row-container',  children=[
            html.Label(children='Escolha o período desejado:'),
            dcc.Dropdown(['Todos os Anos', 'Anos 90', 'Anos 2000', 'Anos 2010'],
                         'Todos os Anos', id='classificacao-etaria'),
        ]),
        dcc.Graph(
            id='comics-rating-graph'
        )
    ])
])

YEAR_COLUMN_TITLE = 'YEAR'


def create_comparative_graphic_column_based(first_df, second_df, first_name, second_name, column_title):
    """Gera um gráfico comparativo entre uma coluna de dois DataFrames

    Args:
      first_df: Primeiro DataFrame a ser utilizado
      second_df: Segundo DataFrame a ser utilizado
      first_name: Nome do primeiro DataFrame
      second_name: Nome do segundo DataFrame
      column_title: Título da coluna em comum entre os DataFrames

    Return:
      Gráfico comparativo entre a coluna dos DataFrames
    """
    values_first_column = get_column(first_df, column_title)
    values_second_column = get_column(second_df, column_title)

    years_first_column = get_column(first_df, YEAR_COLUMN_TITLE)
    years_second_column = get_column(second_df, YEAR_COLUMN_TITLE)

    first_values = unique_value_list(values_first_column)
    second_values = unique_value_list(values_second_column)

    values_in_common = list()
    # Percorre uma das listas de valores
    for value in first_values:
        # Verifica se um valor está na outra lista e não está na values_in_common
        if value in second_values and value not in values_in_common:
            # Adiciona o valor em comum
            values_in_common.append(value)

    @app.callback(
        Output(component_id=f'{column_title}-graph',
               component_property='figure'),
        Input(component_id=f'{column_title}-year', component_property='value')
    )
    def update_comparative_graphic(years_range):
        first_count, second_count = list(), list()
        year_min, year_max = years_range

        iteration = [
            [values_first_column, years_first_column, first_count],
            [values_second_column, years_second_column, second_count]
        ]
        for values_column, years_column, count_list in iteration:
            for value in values_in_common:
                value_count = 0
                # Conta quantas vezes um valor aparece na coluna
                for row_value, row_year in zip(values_column, years_column):
                    if row_value == value and year_max >= row_year >= year_min:
                        value_count += 1
                # Adiciona contagem de um valor
                count_list.append(value_count)
            # Retorna uma lista com a contagem

        graphic_figure = go.Figure([
            go.Bar(name=first_name, x=values_in_common,
                   y=first_count, marker={'color': '#4C9B82'}),
            go.Bar(name=second_name, x=values_in_common,
                   y=second_count, marker={'color': '#0F8BAE'})
        ])
        graphic_figure.update_layout(template='plotly_dark', font={'size': 16})
        return graphic_figure


HAIR_COLUMN_TITLE = 'HAIR'
EYE_COLUMN_TITLE = 'EYE'

create_comparative_graphic_column_based(
    dc_wikia_dataframe, mcu_wikia_dataframe, 'DC', 'MCU', HAIR_COLUMN_TITLE)
create_comparative_graphic_column_based(
    dc_wikia_dataframe, mcu_wikia_dataframe, 'DC', 'MCU', EYE_COLUMN_TITLE)


@app.callback(
    Output('comics-rating-graph', 'figure'),
    Input('classificacao-etaria', 'value')
)
def update_hq_rating_graphic(value):
    if value == "Anos 90":
        graphic = px.pie(values=count90, names=label90,
                         color_discrete_sequence=px.colors.sequential.Emrld)
        ano = 'nos anos 90'
    elif value == "Anos 2000":
        graphic = px.pie(values=count10, names=label10,
                         color_discrete_sequence=px.colors.sequential.Emrld)
        ano = 'nos anos 2000'
    elif value == "Anos 2010":
        graphic = px.pie(values=count20, names=label20,
                         color_discrete_sequence=px.colors.sequential.Emrld)
        ano = 'nos anos 2010'
    else:
        graphic = px.pie(values=rating_counts, names=rating_labels,
                         color_discrete_sequence=px.colors.sequential.Emrld)
        ano = ''

    graphic.update_layout(
        title_text=f'Porcetagem das classificações indicativas dos quadrinhos da Marvel {ano}', template='plotly_dark')
    return graphic


if __name__ == '__main__':
    app.run_server(debug=True)
