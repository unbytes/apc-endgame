from dc_mcu.graphic import hair_graphic, eye_graphic
import sys
from dash import Dash, html, dcc
sys.path.append('./')

app = Dash(__name__)

app.layout = html.Main(children=[
    html.H1(children='Personagens Marvel e DC'),
    html.Div(className="graphic_container", children=[
        html.H2(children='Cor do cabelo'),
        html.Div(className="row-container", children=[
            html.Div([
                "Ano inicial: ",
                dcc.Input(className="year_input",
                          value="1935", type='number', min=1935, max=2013, step=1)]),
            html.Div([
                "Ano final: ",
                dcc.Input(className="year_input",
                          value="2013", type='number', min=1935, max=2013, step=1)])
        ]),
        dcc.Graph(
            id='hair_graph',
            figure=hair_graphic
        )
    ]),
    html.Div(className="graphic_container", children=[
        html.H2(children='Cor dos olhos'),
        html.Div(className="row-container", children=[
            html.Div([
                "Ano inicial: ",
                dcc.Input(className="year_input",
                          value="1935", type='number', min=1935, max=2013, step=1)]),
            html.Div([
                "Ano final: ",
                dcc.Input(className="year_input",
                          value="2013", type='number', min=1935, max=2013, step=1)])
        ]),
        dcc.Graph(
            id='eye_graph',
            figure=eye_graphic
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
