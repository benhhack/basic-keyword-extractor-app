from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from callbacks import get_callbacks
import components


app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])




app.layout = dbc.Container(
    [
        html.H1("Keyword Extraction from Job Description"),
        html.Hr(),
        dbc.Button(
            "Regenerate items",
            color="primary",
            id="button",
            className="mb-3",
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