import io

from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import base64
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
                    value='How many keywords',
                    type="number"
                )
            ]
        ),
        # job description
        html.Div(
            [
                dbc.Label("Job Description"),
                dbc.Textarea(
                    id='text',
                    value='Enter your text here...',
                    style={"height": "200px"}
                )
            ]
        )
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        html.H1("Keyword Extraction from Job Description"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(dcc.Graph(id="frequency-graph"), md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

@app.callback(
    Output("frequency-graph", "figure"),
    [
        Input("top", "value"),
        Input("text", "value"),
    ],
)
def make_graph(text, top):

    if text and top:
        df = keyword_extraction.get_keywords(text,top)

        data = go.bar(df, x='keyword', y='count')

        layout = {"xaxis": {"title": f"Top {top} Words in Job Description"}, "yaxis": {"title": "Number of Occurrences"}}

        return go.Figure(data=data, layout=layout)

    return ""




if __name__ == '__main__':
    app.run_server(debug=True)