from dash import Dash, html, dcc, Input, Output
import plotly.express as px

from mcu_comics.graphic import count90, label90, count10, label10, count20, label20, rating_counts, rating_labels

import sys
sys.path.append('./')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Classificação Etária das HQs'),
    html.H2(children='Gráficos com as classificações.'),
    html.Div(children='Interação referente às classificações etárias.'),
    dcc.Dropdown(['Todos os Anos', 'Anos 90', 'Anos 2000', 'Anos 2010'],
                 'Todos os Anos', id='classificacao_etaria'),
    dcc.Graph(id='grafico_interação')
])


@app.callback(
    Output('grafico_interação', 'figure'),
    Input('classificacao_etaria', 'value')
)
def graphic_hq_rating(value):
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

    graphic.update_layout(title_text=f'Porcetagem das classificações indicativas dos quadrinhos da Marvel {ano}', template='plotly_dark')
    return graphic

if __name__ == '__main__':
    app.run_server(debug=True)
