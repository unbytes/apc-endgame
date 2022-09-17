from dc_mcu.graphic import hair_graphic, eye_graphic
import sys
from dash import Dash, html, dcc
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
                                id='hair-year', className='year-slider',
                                tooltip={"placement": "bottom", "always_visible": True})
            ]),
            dcc.Graph(
                id='hair-graph',
                figure=hair_graphic
            )
        ]),
        html.Div(className='column-container', children=[
            html.H1('Cor dos olhos'),
            html.Div(className='row-container', children=[
                html.Label('Escolha o intervalo (Anos):'),
                dcc.RangeSlider(min=1935, max=2013, marks=None, step=1, value=[1935, 2013],
                                id='eye-year', className='year-slider',
                                tooltip={"placement": "bottom", "always_visible": True})
            ]),
            dcc.Graph(
                id='eye-graph',
                figure=eye_graphic
            )
        ])
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
