import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ClientsideFunction, State

import numpy as np
import pandas as pd
from datetime import datetime as dt
import dash_components
import data
import dash_bootstrap_components as dbc
import scatterplot
import heatmapfig
import Paragraphs
import clustered_barchart
import choropleth_map
import map_barCharts

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport",
                "content": "width=device-width,initial-scale=1"}],
)

app.title = "The State of the World’s Children- UNICEF"

server = app.server
app.config.suppress_callback_exceptions = True

mapdata = pd.read_csv('./data/UNICEF_Data_Imp.csv')
VarList = data.variables(mapdata)
bardata = pd.read_csv('./data/UNICEF_Data_Imp.csv', index_col=0, thousands=',')

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

clusteredBarData = data.getDataBarChart()
ClusteredbarChart = clustered_barchart.draw_clusteredBarchart(clusteredBarData)
explainClustBar = Paragraphs.ExplainClustBarViz()
explainVis1 = Paragraphs.descrptionViz1()
explainVis2 = Paragraphs.ExplainVis2()
introduction = Paragraphs.introduction()
explainReductionRate = Paragraphs.ExplainMapReductionRate()


def description_card():
    return html.Div(
        id="description-card",
        children=[
            html.H1("The State of the World’s Children - UNICEF ",
                    style={'color': '#2c8cff'}),
            html.Div(
                id="intro",
                children=introduction,
            ),
        ],
    )


app.layout = html.Div(
    id="app-container",
    style={'backgroundColor': 'white', 'margin': 0,
           'padding': "10px 90px 20px 90px"},
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("polymtl.png"),
                               style={"height": "50px"})],
        ),

        html.Div(
            children=[description_card()] +
                     [
                         html.Div(
                             ["initial child"], id="output-clientside",
                             style={"display": "none"}
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
                        html.Hr(style={"background-color": "gray", "height": "2px"}),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(dcc.Dropdown(id='map-dropdown',
                                                 options=VarList,
                                                 value=VarList[0]["value"]),
                                    width=6)]),
                        html.Br(),
                        dbc.Row(explainVis1),
                        html.Br(),
                        dbc.Row([dcc.Graph(id='display-selected-values')]),
                        html.Br(),
                        dbc.Row(explainReductionRate),
                        dbc.Row([
                            dbc.Col(dcc.Graph(
                                id='bar-chart',
                                className='graph',
                                figure=map_barCharts.get_empty_figure('barchart'),
                                config=dict(
                                    scrollZoom=False,
                                    showTips=False,
                                    showAxisDragHandles=False,
                                    doubleClick=False,
                                    displayModeBar=False
                                ))),
                            dbc.Col(dcc.Graph(
                                id='b2b-chart',
                                className='graph',
                                figure=map_barCharts.get_empty_figure('b2bchart'),
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
                        html.Hr(style={"background-color": "gray", "height": "2px"}),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(dash_components.generate_country_dropdown(data.getCountriesDataVis2()), width=3),
                            dbc.Col(dash_components.generate_info_panel2(), width={"size": 3, "offset": 1})
                        ]
                        ),
                        html.Br(),
                        dbc.Row(explainVis2),
                        html.Br(),
                        dbc.Row(
                            [dbc.Col(dash_components.generate_vis2(data.getDataVis2DataFrame()))]
                        ),
                        html.Br(),

                        dbc.Row(dcc.Graph(
                            figure=ClusteredbarChart,
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False
                            ),
                            className='graph',
                            id='clustBar-chart'
                        )),
                        html.Br(),
                        dbc.Row(explainClustBar),

                        html.Br(),
                        html.H2("Vaccinations"),
                        html.Hr(style={"background-color": "gray", "height": "2px"}),
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
                                 dbc.Col([dbc.Row(init4b),
                                          dbc.Row(dcc.Dropdown(id="dropdown",
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


# choropleth map according to the selected variable
@app.callback(Output('display-selected-values', 'figure'),
              [Input('map-dropdown', 'value')])
def update_output(value):
    df = pd.read_csv('./data/UNICEF_Data_Imp.csv')
    df = data.to_float(df, value)
    fig = choropleth_map.get_map(df, value, VarList)
    return fig


# display bar charts when a country is clicked
# or drop down menu selection changed
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('b2b-chart', 'figure')],
    [Input('display-selected-values', 'clickData'),
     Input('map-dropdown', 'value')]
)
def map_clicked(clickData, value):
    if clickData is None:
        b2b_figure = map_barCharts.get_empty_figure('b2bchart')
        bar_figure = map_barCharts.get_empty_figure('barchart')
        return bar_figure, b2b_figure

    selectCategory = value  # get value of selection from drop-down menu
    country = clickData['points'][0]['hovertext']  # get name of clicked country

    # construct the dataframe containing top 5 & bottom 5 countries
    # then add the clicked country to the dataframe
    sorted_df, top_bottom_data = data.top_bottom(bardata, selectCategory)
    top_bottom_country, clickedCountry = data.insert_country(sorted_df, top_bottom_data, country)

    # plot horizontal bar chart for selected category
    # plot back-to-back chart only if selected category is Mortality Rate (under 5)
    bar_figure = map_barCharts.draw_barchart(top_bottom_country, selectCategory, clickedCountry)
    if selectCategory == 'Under-five mortality rate 2019':
        b2b_figure = map_barCharts.draw_b2bchart(top_bottom_country, clickedCountry)
    else:
        b2b_figure = map_barCharts.get_empty_figure('b2bchart')

    return bar_figure, b2b_figure


@app.callback([Output('scatter', 'figure')],
              [Input('dropdown', 'value')])
def display(DD):  # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    scatter = heatmapfig.initScatter(countries, DD, VaccList)

    return [scatter]


# update the scatter matrix and info panel when a country is clicked
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
def countrySelected(clicks_fig, value):
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
        country, ageGroup, rates = info_details(country)
        rate1, rate2, rate3, rate4, rate5 = rates
        group1, group2, group3, group4, group5 = ageGroup
        return group1, group2, group3, group4, group5, rate1, rate2, rate3, rate4, rate5, {
            'visibility': 'visible'}, scatterplot.update_vis2(data.getDataVis2DataFrame(), country), [country]
    return None, None, None, None, None, None, None, None, None, None, {
        'visibility': 'hidden'}, scatterplot.add_scatter_matrix(data.getDataVis2DataFrame()), [None]


def info_details(country):
    dataPerCountry = data.getDataPerCountry(country)
    rates = dataPerCountry.iloc[[0]].values.tolist()[0][2:]
    ageGroup = list(dataPerCountry.columns)[2:]
    # order based on mortality rate
    zipped_lists = zip(rates, ageGroup)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    rates, ageGroup = [list(tuple) for tuple in tuples]

    return country, ageGroup, rates

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
