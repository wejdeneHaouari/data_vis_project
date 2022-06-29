from dash import dcc
from dash import html
import plotly.express as px

import data


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
