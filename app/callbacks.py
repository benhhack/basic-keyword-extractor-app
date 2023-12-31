from dash import Input, Output, State, html
import dash_bootstrap_components as dbc
from keyword_extraction import get_keywords
from create_wordcloud import make_cloud

from io import BytesIO
import base64


def make_table(text, top):
    df = get_keywords(text, top)
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)


def get_callbacks(app):
    @app.callback(
        Output("tab-content", "children"),
        Input("tabs", "active_tab"),
        Input("store", "data"),
    )
    def render_tab_content(active_tab, data):
        """
        This callback takes the 'active_tab' property as input, as well as the
        stored graphs, and renders the tab content depending on what the value of
        'active_tab' is.
        """
        if active_tab and data is not None:
            if active_tab == "table-tab":
                return data["table"]
            elif active_tab == "wc-tab":
                return html.Img(src=data['wc'])
        return "Input your job description and number of keywords and press generate. "

    @app.callback(
        Output("store", "data"),
        Input("gen-button", "n_clicks"),
        State("textinp", "value"),
        State("top", "value")
    )
    def gen_review(n_clicks, text, top):
        """
        :param n_clicks:
        :param text: the user input of the job description
        :param top: the top n keywords that a user wants
        :return: the table object ordered by most relevant
        """
        if not (n_clicks and text and top):
            # TODO: Make an alert
            return None

        img = BytesIO()
        make_cloud(text).save(img, format='PNG')

        # wordcloud = make_wordcloud()
        return {"table": make_table(text, top), "wc": 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())}
