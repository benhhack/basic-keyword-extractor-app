from dash import html
import dash_bootstrap_components as dbc

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
                dbc.Input(
                    id='textinp',
                    value='Enter your text here...',
                    type='text',
                    style={"height": "200px"}
                )
            ]
        )
    ],
    body=True,
)

graph_tabs = dbc.Tabs(
    [
        dbc.Tab(label='Table', tab_id='table-tab'),
        dbc.Tab(label='Chart', tab_id='chart-tab'),
        dbc.Tab(label='WordCloud', tab_id='wc-tab')
    ],
    id='tabs',
    active_tab="table-tab"
)