import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ClientsideFunction, State

import json
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
import heatmapfig
import Paragraphs
import clustered_barchart
import preprocess
import choropleth_map
import bar_charts


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.title = "The State of the World’s Children- UNICEF"

server = app.server
app.config.suppress_callback_exceptions = True

mapdata = pd.read_csv('./assets/UNICEF_Data_Imp.csv')
VarList = preprocess.variables(mapdata)
my_data=pd.read_csv('./assets/UNICEF_Data_Imp.csv', index_col=0, thousands=',')

data_path = "data/UNICEF_Data_4.xlsx"
regional = data.getData(data_path, "Regions")

countries = data.getData(data_path, "Countries")
VaccList = data.Vaccines(regional)

heatmap = heatmapfig.getHeatmap(regional)
scatter = heatmapfig.initScatter(countries, "Rotavirus", VaccList)

comments4a = Paragraphs.descriptionViz4a()
comments4b = Paragraphs.descriptionViz4b()
explain4a = Paragraphs.ExplainViz4a()
init4b = Paragraphs.InitViz4b()

barChartData = data.getDataBarChart()

barchart = clustered_barchart.draw_barchart(barChartData)


def description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H1("The State of the World’s Children - UNICEF ", style={'color': '#2c8cff'}),
            html.Div(
                id="intro",
                children="According to UNICEF, at least 1 in 3 children under five is under/overweight, and 1 in 2 experience hidden hunger which lessens the ability of millions of children to grow and develop healthily leading to their death. The following charts shows mortality and vaccination of children around the world",
            ),
        ],
    )



app.layout = html.Div(
    id="app-container",
    style={'backgroundColor': 'white', 'margin': 0, 'padding':"10px 90px 20px 90px"},
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("polymtl.png"), style={"height":"50px"})],
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
                        html.Br(),
                        html.H2("Child Mortality World Wide"),
                        html.Hr(),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(dcc.Dropdown(id='map-dropdown', options=VarList, value=VarList[0]["value"]), width=3)]),
                            #dbc.Row([dcc.Dropdown(id='map-dropdown', options=VarList, value=VarList[0]["value"])],
                            #style={'width': '48%', 'display': 'inline-block'}),
                            html.Br(),
                            html.Br(),
                            dbc.Row([dcc.Graph(id='display-selected-values')]),
                            dbc.Row([
                                    dbc.Col(dcc.Graph(
                                                    id='bar-chart',
                                                    className='graph',
                                                    figure=bar_charts.get_empty_figure('barchart'), 
                                                    #style={'width': '60vh', 'height': '30vh'},
                                                    config=dict(
                                                        scrollZoom=False,
                                                        showTips=False,
                                                        showAxisDragHandles=False,
                                                        doubleClick=False,
                                                        displayModeBar=False
                                                    ))),
                                    dbc.Col( dcc.Graph(
                                                    id='b2b-chart',
                                                    className='graph',
                                                    figure=bar_charts.get_empty_figure('b2bchart'), #draw_barchart(top_bottom_country, column, clickedCountry)
                                                    #style={'width': '60vh', 'height': '30vh'},
                                                    config=dict(
                                                        scrollZoom=False,
                                                        showTips=False,
                                                        showAxisDragHandles=False,
                                                        doubleClick=False,
                                                        displayModeBar=False
                                                    )))
                                    ]),
                        html.Br(),
                        html.H2("Trends"),
                        html.Hr(),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(dash_components.generate_country_dropdown(data.getCountriesDataVis2()), width=3),
                            dbc.Col(dash_components.generate_info_panel2(), width={"size": 3, "offset": 1})
                        ]
                        ),

                        dbc.Row(
                            [dbc.Col(dash_components.generate_vis2(data.getDataVis2DataFrame()))]
                        ),
                        html.Br(),
                        html.Br(),
                        dbc.Row([
                            dcc.Graph(
                                figure=barchart,
                                #style={'width': '60vh', 'height': '60vh'},
                                config=dict(
                                    scrollZoom=False,
                                    showTips=False,
                                    showAxisDragHandles=False,
                                    doubleClick=False,
                                    displayModeBar=False
                                ),
                                className='graph',
                                id='line-chart'
                            )
                        ]),
                        html.Br(),
                        html.H2("Vaccinations"),
                        html.Hr(),
                        html.Br(),
                        dbc.Row(
                            [dbc.Col(dcc.Graph(figure=heatmap, id='heatmap',
                                               config=dict(
                                                   showTips=False,
                                                   showAxisDragHandles=False,
                                                   displayModeBar=False)),
                                     ),
                             dbc.Col(explain4a)
                             ]
                        ),
                        dbc.Row(comments4a),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row([dbc.Col(dcc.Graph(figure=scatter, id='scatter',
                                                   config=dict(
                                                       showTips=False,
                                                       showAxisDragHandles=False,
                                                       displayModeBar=False))),
                                 dbc.Col([dbc.Row(init4b),dbc.Row(dcc.Dropdown(id="dropdown",
                                                  options=VaccList,
                                                  value=VaccList[0]["value"]))])]
                                ),
                        dbc.Row(comments4b)
                    ],
                )
            ],
        ),
    ],
)






@app.callback(Output('display-selected-values', 'figure'),
              [Input('map-dropdown', 'value')])
def update_output(value):
    data = pd.read_csv('./assets/UNICEF_Data_Imp.csv')
    df = preprocess.to_float(data, value)
    fig = choropleth_map.get_map(df, value, VarList)
    return fig



@app.callback(
    [Output('bar-chart', 'figure'),Output('b2b-chart','figure')],
    [Input('display-selected-values', 'clickData'),Input('map-dropdown', 'value')] 
)
def map_clicked(clickData,value):
    
    
    if clickData is None:
        b2b_figure=bar_charts.get_empty_figure('b2bchart')
        figure = bar_charts.get_empty_figure('barchart')
        return figure,b2b_figure
    
    columnb=value
    country=clickData['points'][0]['hovertext']
    
    sorted_df, top_bottom_data=preprocess.top_bottom(my_data, columnb)
    top_bottom_country, clickedCountry=bar_charts.insert_country(sorted_df, top_bottom_data, country) 

    figure=bar_charts.draw_barchart(top_bottom_country, columnb, clickedCountry)
    
    b2b_figure=bar_charts.get_empty_figure('b2bchart')
    if columnb=='Under-five_mortality_rate_2019,both':
        b2b_figure=bar_charts.draw_b2bchart(top_bottom_country, clickedCountry)
    
    return figure,b2b_figure
  


@app.callback([Output('scatter', 'figure')],
              [Input('dropdown', 'value')])
def display(DD):  # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    scatter = heatmapfig.initScatter(countries, DD, VaccList)

    return [scatter]


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
    app.run_server()