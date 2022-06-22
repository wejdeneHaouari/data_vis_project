'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
from dash import dcc
from dash import html
import plotly.express as px

import data


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    style = {'visibility': 'hidden',
             'border': '1px solid black',
             'padding': '10px'}
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme,
                       style):  # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers

    # get the color of the marker
    color = figure['layout']['template']['layout']['colorway'][curve]
    title = figure['data'][curve]['customdata'][0][point]
    title = html.P(title, style={'color': color})
    # get the mode for the figure
    mode = figure['data'][curve]['customdata'][1][point]
    theme = None
    # if marker have theme then we add thematic
    if figure['data'][curve]['customdata'][2][point]:
        themeList = figure['data'][curve]['customdata'][2][point].split()
        theme = [
            html.P('Thématique:'),
            html.Ul([html.Li(x) for x in themeList])
        ]
    # set
    style = {'visibility': 'visible',
             'border': '1px solid black',
             'padding': '10px'}
    return title, mode, theme, style


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
