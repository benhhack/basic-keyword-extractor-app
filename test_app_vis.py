
from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=10)

def test_buttons_exist(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-buttons", timeout=10)


