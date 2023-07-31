from dash import Input, Output
import dash_bootstrap_components as dbc
from keyword_extraction import get_keywords


def get_callbacks(app):
    @app.callback(
        Output("df-table", "children"),
        [
            Input("textinp", "value"),
            Input("top", "value")
        ]
    )
    def make_table(text, top):
        """
        :param text: the user input of the job description
        :param top: the top n keywords that a user wants
        :return: the table object ordered by most relevant
        """
        if text and top:
            df = get_keywords(text, top)
            return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

