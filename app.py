import io

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

import keyword_extraction

app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

return_table = dbc.Table(

)

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
        # this is for tabs, come back to this later
        # dbc.Row(
        #     [
        #         dbc.Col(inputs, md=4),
        #         dbc.Col(
        #             [
        #                 graph_tabs,
        #                 html.Div(id="tab-content", className='p-4')
        #             ]),
        #
        #     ],
        #     align="center",
        # ),
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(dbc.Table(id='df-table'), md=8)
            ],
            align = 'centre'
        )
    ],
    fluid=True,
)

@app.callback(
    Output("df-table", "children"),
    [
        Input("textinp", "value"),
        Input("top", "value")
    ]
)
def make_table(text, top):
    if text and top:
        df = keyword_extraction.get_keywords(text, top)
        return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

# @app.callback(
#     Output("tab-content", "children"),
#     [Input("tabs", "active_tab"), Input("textinp", "txt"), Input("top", "value")],
# )
# def render_tab_context(active_tab, txt, value):
#     """
#     :param active_tab: input property
#     :param data:
#     :return:
#     """
#     if active_tab and txt is not None and value is not None:
#         df= keyword_extraction.get_keywords(txt, value)
#         if active_tab == "table-tab":
#             return dbc.Table.from_dataframe(df)
#         elif active_tab == "chart-tab":
#             return dcc.Graph(id='freq-chart')
#     return "No tab selected"





if __name__ == '__main__':
    app.run_server(debug=True)