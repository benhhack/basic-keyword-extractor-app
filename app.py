import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("./data/preprocessed.csv")

fig = px.line(df, 'date', 'sales')

app.layout = html.Div(children=[
    html.H1(children='Date vs Sales'),

    html.Div(children='''
        Graphing sales of pink morsels against the date
    '''),

    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
