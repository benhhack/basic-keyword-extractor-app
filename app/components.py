from dash import html
import dash_bootstrap_components as dbc

button = html.Div(dbc.Button(
            "Generate review",
            color="primary",
            id="gen-button",
            className="mb-3",
            n_clicks=0
        ), style={"height": "10px"})

inputs = dbc.Card(
    [
        # number of keywords
        html.Div(
            [
                dbc.Label("Top N Keywords"),
                dbc.Input(
                    id='top',
                    value=10,
                    type="number"
                )
            ]
        ),
        # job description
        html.Div(
            [
                dbc.Label("Job Description"),
                dbc.Textarea(
                    id='textinp',
                    value='Enter your text here...',
                    style={"height": "200px"}
                )
            ]
        )
    ],
    body=True,
)

graph_tabs = [dbc.Tabs(
    [
        dbc.Tab(label='Table', tab_id='table-tab'),
        # dbc.Tab(label='Chart', tab_id='chart-tab'),
        dbc.Tab(label='WordCloud', tab_id='wc-tab')
    ],
    id='tabs',
    active_tab="table-tab"
),
html.Div(id="tab-content", className="p-4")]