import pandas as pd
import pathlib

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

dataframeVis2 = pd.read_excel(DATA_PATH.joinpath("UNICEF_Data.xlsx"), sheet_name="dataViz2")
# sort by country alphabetically
dataframeVis2 = dataframeVis2.sort_values('country').reset_index()
dataBarChart = pd.read_csv('./data/Regions.csv')


def getDataVis2DataFrame():
    return dataframeVis2


def getCountriesDataVis2():
    return dataframeVis2['country']


def getDataPerCountry(country):
    return dataframeVis2[dataframeVis2['country'] == country]


def getData(path, loc):
    Sheet = "DataViz4_" + loc
    df = pd.read_excel(path, sheet_name=Sheet, index_col=loc)
    names = pd.read_excel(path, "DataViz4_VaccineNames")
    for name in names.to_dict('records'):
        df.rename(columns={name["ShortName"]: name["LongName"]}, inplace=True)
    df.drop(columns=["HighLevel", "Diphtheria, Pertussis, Tetanus, 1/3"],
            index=["Least developed countries", "Europe and Central Asia",
                   "Sub-Saharan Africa"], errors="ignore",
            inplace=True)
    df = df.sort_index(axis=1)
    df = df.replace("-", "")

    return df


def Vaccines(df):
    value = list(df.columns)
    label = pd.Series(value)
    label = label.replace(
        {"Haemoph. influenzae": "Haemophilus influenzae", "Strept. pneumoniae": "Streptococcus pneumoniae",
         "DTP Combination¹": "Diphteria, Tetanus, Pertussis"})
    # label = label.replace({"Haemoph. influenzae":"Haemophilus influenzae", "Strept. pneumoniae":"Streptococcus pneumoniae"})
    label = label.to_list()
    vaccines = []
    for i in range(0, len(label)):
        vaccines.append(dict(label=label[i], value=value[i]))

    return vaccines


def getDataBarChart():
    return dataBarChart
