import pandas as pd
from dash import Dash, html, dcc,  Output, Input,dash_table
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("./data/preprocessed.csv")

fig = px.line(df, 'date', 'sales')

app.layout = html.Div(
    style={'font-family': 'Arial, sans-serif', 'margin': '20px'},
    children=[
        html.H1(
            children='Date vs Sales',
            style={'text-align': 'center', 'margin-bottom': '20px'}
        ),

        html.Div(
            children=[
                dcc.Graph(
                    id='graph',
                    figure=px.line(df, 'date', 'sales')
                )
            ],
            style={'margin-bottom': '30px'}
        ),

        html.Div(
            children=[
                html.P('Choose which region you would like to view:', style={'margin-bottom': '10px'}),
                dcc.RadioItems(
                    id='radio-buttons',
                    options=[
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                        {'label': "All", 'value': "None"}
                    ],
                    value=None,
                    labelStyle={'display': 'block', 'margin-right': '10px'}
                )
            ],
            style={'margin-bottom': '30px'}
        )
    ]
)

@app.callback(
    Output('graph', 'figure'),
    [Input('radio-buttons', 'value')]
)

def update_graph(selected_region):
    if selected_region == 'None':
        fig = px.line(df, 'date', 'sales')
    else:
        filtered_df = df[df['region']==selected_region]
        fig = px.line(filtered_df, 'date', 'sales')

    return fig

if __name__ == '__main__':
    app.run(debug=True)
