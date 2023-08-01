from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc
from callbacks import get_callbacks
import components


app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])




app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.H1("Keyword Extraction from Job Description"),
        html.Hr(),
        dbc.Button(
            "Generate review",
            color="primary",
            id="gen-button",
            className="mb-3",
            n_clicks=0
        ),

        dbc.Row(
            [
                dbc.Col(components.inputs, md=4),
                dbc.Col(dbc.Table(id='df-table'), md=8)
            ],
            align = 'centre'
        )
    ],
    fluid=True,
)



get_callbacks(app)





if __name__ == '__main__':
    app.run_server(debug=True)