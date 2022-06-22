import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ClientsideFunction, State

import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib
import dash_components
import data
import callback
import dash_bootstrap_components as dbc
import scatterplot

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "The State of the World’s Children- UNICEF"

server = app.server
app.config.suppress_callback_exceptions = True


def description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H3("The State of the World’s Children- UNICEF ", style={'color': '#2c8cff'}),
            html.Div(
                id="intro",
                children="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            ),
        ],
    )


app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("polymtl.png"))],
        ),

        html.Div(
            children=[
                         description_card()]
                     + [
                         html.Div(
                             ["initial child"], id="output-clientside", style={"display": "none"}
                         )
                     ],
        ),

        html.Div(
            children=[
                # Patient Volume Heatmap
                html.Div(
                    id="vis2layout",
                    children=[
                        html.B("Trends"),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col(dash_components.generate_country_dropdown(data.getCountriesDataVis2()), width=3),
                            dbc.Col(dash_components.generate_info_panel2(), width={"size": 3, "offset": 1})
                        ]
                        ),

                        dbc.Row(
                            [dbc.Col(dash_components.generate_vis2(data.getDataVis2DataFrame())),

                             ]
                        )
                    ],
                )
            ],
        ),
    ],
)


@app.callback([Output('group1', 'children'),
               Output('group2', 'children'),
               Output('group3', 'children'),
               Output('group4', 'children'),
               Output('group5', 'children'),
               Output('rate1', 'children'),
               Output('rate2', 'children'),
               Output('rate3', 'children'),
               Output('rate4', 'children'),
               Output('rate5', 'children'),
               Output('info-panel-vis2', 'style'),
               Output('graph', 'figure'),
               [Output('country-select', 'value')]],
              [Input('graph', 'clickData'),
               Input('country-select', 'value')])
def callback_a(clicks_fig, value):
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id
    # clique on the graph
    if triggered_id == 'graph':
        return graphClique()
    if triggered_id == 'country-select':
        return countrySelect(value)
    else:
        return None, None, None, None, None, None, None, None, None, None, {
            'visibility': 'hidden'}, scatterplot.add_scatter_matrix(data.getDataVis2DataFrame()), [None]


def graphClique():
    ctx = dash.callback_context
    if not ctx.triggered:
        return None, None, None, None, None, None, None, None, None, None, {
            'visibility': 'hidden'}, scatterplot.add_scatter_matrix(data.getDataVis2DataFrame()), [None]
    if ctx.triggered[0]['prop_id'].split('.')[0] == 'graph':
        country = ctx.triggered[0]['value']['points'][0]['customdata']
        country, ageGroup, rates = callback.info_details(country)
        rate1, rate2, rate3, rate4, rate5 = rates
        group1, group2, group3, group4, group5 = ageGroup
        return group1, group2, group3, group4, group5, rate1, rate2, rate3, rate4, rate5, {
            'visibility': 'visible'}, scatterplot.update_vis2(data.getDataVis2DataFrame(), country), [country]
    return None, None, None, None, None, None, None, None, None, None, {
        'visibility': 'hidden'}, scatterplot.add_scatter_matrix(data.getDataVis2DataFrame()), [None]


def countrySelect(value):
    if value:
        dataPerCountry = data.getDataPerCountry(value)
        rates = dataPerCountry.iloc[[0]].values.tolist()[0][2:]
        ageGroup = list(dataPerCountry.columns)[2:]
        # order based on mortality rate
        zipped_lists = zip(rates, ageGroup)
        sorted_pairs = sorted(zipped_lists, reverse=True)
        tuples = zip(*sorted_pairs)
        rates, ageGroup = [list(tuple) for tuple in tuples]
        rate1, rate2, rate3, rate4, rate5 = rates
        group1, group2, group3, group4, group5 = ageGroup
        return group1, group2, group3, group4, group5, rate1, rate2, rate3, rate4, rate5, {
            'visibility': 'visible'}, scatterplot.update_vis2(data.getDataVis2DataFrame(),
                                                              value), [value]
    return None, None, None, None, None, None, None, None, None, None, {
        'visibility': 'hidden'}, scatterplot.add_scatter_matrix(
        data.getDataVis2DataFrame()), [None]


# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
