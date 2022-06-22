import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

dataframeVis2 = pd.read_excel(DATA_PATH.joinpath("UNICEF_Data.xlsx"), sheet_name="dataViz2")
# sort by country alphabetically
dataframeVis2 = dataframeVis2.sort_values('country').reset_index()



def getDataVis2DataFrame():
    return dataframeVis2


def getCountriesDataVis2():
    return dataframeVis2['country']


def getDataPerCountry(country):
    return dataframeVis2[dataframeVis2['country'] == country]
