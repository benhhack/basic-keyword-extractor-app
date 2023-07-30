from dash import Dash, dcc, html, dash_table, Output, Input
import pandas as pd
from wordcloud import WordCloud
import base64

# Sample DataFrame for displaying results (you can replace this with your actual extracted keywords/phrases)
data = {
    'Keyword/Phrase': ['keyword1', 'keyword2', 'keyword3'],
    'Value': [0.8, 0.7, 0.6]
}
df = pd.DataFrame(data)

# Sample word cloud image (you can replace this with your actual word cloud image)
wordcloud_image = 'cloud.png'

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Keyword Extractor"),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '100px',
            'lineHeight': '100px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '20px'
        },
        multiple=False
    ),

    html.Div(id='output-data', style={'margin': '20px'}),

    dcc.Graph(
        id='word-cloud',
        figure={
            'data': [{
                'type': 'scatter',
                'x': [0, 1],
                'y': [0, 1],
                'mode': 'text',
                'text': ['Sample', 'WordCloud'],
                'textfont': {
                    'size': 20,
                    'color': '#1f77b4'
                }
            }],
            'layout': {
                'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                'height': 400,
                'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0},
                'plot_bgcolor': '#fff',
                'paper_bgcolor': '#fff'
            }
        },
        style={'margin': '20px'}
    )
])

def parse_contents(contents, filename):
    # Process the uploaded file and extract keywords/phrases (you can implement your extraction logic here)
    # For this example, we'll just return the sample DataFrame.
    return df

@app.callback(Output('output-data', 'children'),
              Output('word-cloud', 'figure'),
              Input('upload-data', 'contents'),
              Input('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        df = parse_contents(contents, filename)
        # Generate word cloud image (you can use your own word cloud generation logic here)
        with open(wordcloud_image, 'rb') as f:
            encoded_image = base64.b64encode(f.read()).decode()
        word_cloud_figure = {
            'data': [{
                'type': 'scatter',
                'x': [0, 1],
                'y': [0, 1],
                'mode': 'text',
                'text': ['Sample', 'WordCloud'],
                'textfont': {
                    'size': 20,
                    'color': '#1f77b4'
                }
            }],
            'layout': {
                'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                'height': 400,
                'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0},
                'images': [{
                    'source': 'data:image/png;base64,{}'.format(encoded_image),
                    'xref': 'x',
                    'yref': 'y',
                    'x': 0.5,
                    'y': 0.5,
                    'sizex': 0.8,
                    'sizey': 0.8,
                    'sizing': 'stretch',
                    'opacity': 0.8,
                    'layer': 'above'
                }],
                'plot_bgcolor': '#fff',
                'paper_bgcolor': '#fff'
            }
        }
        return [
            html.H3("Keywords/Phrases and Values"),
            dash_table.DataTable(
                id='table',
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records')
            ),
            word_cloud_figure
        ]
    return '', {}


if __name__ == '__main__':
    app.run_server(debug=True)