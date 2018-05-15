import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import json

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='heatmap',
        figure={
            'data': [{
                'z': [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ],
                'text': [
                    ['a', 'b', 'c'],
                    ['d', 'e', 'f'],
                    ['g', 'h', 'i']
                ],
                'customdataa': [
                    ['c-a', 'c-b', 'c-c'],
                    ['c-d', 'c-e', 'c-f'],
                    ['c-g', 'c-h', 'c-i'],
                ],
                'type': 'heatmap'
            }]
        }
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('heatmap', 'hoverData'),
     Input('heatmap', 'clickData')])
def display_hoverdata(hoverData, clickData):
    return [
        json.dumps(hoverData, indent=2),
        html.Br(),
        json.dumps(clickData, indent=2)
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
