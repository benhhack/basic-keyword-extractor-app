# from contextvars import copy_context
# from dash._utils import AttributeDict
#
# from dash import html, Dash
# import pytest
from app import app

def test_components():
    test_client = app.test_client()

    # Get the response of the app layout
    response = test_client.get('/')

    # Assert that the header with "Date vs Sales" is present in the response
    assert b'Date vs Sales' in response.data
    print("Response data in app")

    # assert the graph is in the response
    assert b'graph' in response.data
    print("Graph in app")

    # assert the radio buttons are in the response
    assert  b'radio-buttons' in response.data
    print("Radio buttons in app")


