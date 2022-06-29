import pandas as pd
import pathlib

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

dataframeVis2 = pd.read_excel(DATA_PATH.joinpath("UNICEF_Data.xlsx"), sheet_name="dataViz2")
# sort by country alphabetically
dataframeVis2 = dataframeVis2.sort_values('country').reset_index()
dataBarChart = pd.read_csv('./data/Regions.csv')



def to_float(my_df, column):  # ="Under-five_mortality_rate_2019,both"
    '''
        Convert columns to float
        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    try:
        my_df[column] = my_df[column].astype(float)
    except ValueError:
        print("CAnnot convert to float")
        my_df[column] = my_df[column].str.replace(',', '').astype(float)
    return my_df


def variables(my_df):
    my_df.drop(columns=["Unnamed: 0", "Country", "country_code",
                        "Under-five mortality rate 2019, male",
                        "Under-five mortality rate 2019, Female"],
               errors="ignore", inplace=True)
    value = list(my_df.columns)
    label = pd.Series(value)
    label = label.replace({"Under-five mortality rate 2019,both": "Mortality rate (under five)",
                            "Neonatal mortality rate 2019": "Mortality rate (Neonatal)",
                            "Infant mortality rate 2019": "Mortality rate (Infant)",
                            "Mortality rate among children aged 5–14 years, 2019": "Mortality rate (5-14 years)",
                            "Annual rate of reduction in under-five mortality rate\t": "Annual percentage of reduction for mortality rate (under five)",
                            "Annual rate of reduction in stillbirth rate": "Annual percentage of reduction for mortality rate (stillbirth)",
                            "Under five deaths 2019": "Number of deaths (under five)",
                            "Deaths among children aged 5–14 years 2019": "Number of deaths (5-14 years)"})
    label = label.to_list()
    variables = []
    for i in range(0, len(label)):
        variables.append(dict(label=label[i], value=value[i]))   
    return variables



#get the label of the selected group from the drop-down menu
#this function is called to get the display title (label) for the bar chart
def get_selected_group_label(selectedGroup,top_bottom_country):
    
    columns_dict=variables(top_bottom_country)
    groupLabel=[x['label'] for x in columns_dict if selectedGroup==x['value']][0]
    #print('column=',columnb)
    return groupLabel


#this function gets the top 5 countries (highest mortality) and bottom 5 countries (lowest mortality) for the selected category

def top_bottom(my_df, selectCategory):
    my_df = my_df.dropna(axis=0)
    my_df['Under-five mortality rate 2019, male'] = my_df['Under-five mortality rate 2019, male'].astype(int)
    my_df['Under-five mortality rate 2019, Female'] = my_df['Under-five mortality rate 2019, Female'].astype(int)
    print('before')
    my_df[selectCategory] = pd.to_numeric(my_df[selectCategory])
    print('after')

    sorted_df = my_df.sort_values(by=[selectCategory], ascending=False, 
                                  ignore_index=True)
    sorted_df = sorted_df[['Country', selectCategory,
                           'Under-five mortality rate 2019, male',
                           'Under-five mortality rate 2019, Female']]
    sorted_df['numCountry'] = ""
    for index, row in sorted_df.iterrows():
        sorted_df.loc[index, 'numCountry'] = \
                      str(index+1)+'.' + sorted_df.loc[index, 'Country']
    top = sorted_df.iloc[-5:, :]
    top_bottom_data = top.append(sorted_df.iloc[0:5, :])    
    top_bottom_data = top_bottom_data.sort_index(ascending=False)
    return sorted_df, top_bottom_data


def getDataVis2DataFrame():
    return dataframeVis2


def getCountriesDataVis2():
    return dataframeVis2['country']


def getDataPerCountry(country):
    return dataframeVis2[dataframeVis2['country'] == country]

#gets the vaccination data for regional or country resolution
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


# adding the selected country to the chart data 
def insert_country(sorted_df, top_bottom_data, country):
     #default order for country if not one of the top 5 or bottom 5
    clickedCountry = 5
    
    #search for country name in the sorted top 5 and bottom 5 countries (top_bottom_data) and return order 
    ind = top_bottom_data.index.get_indexer_for((top_bottom_data[
                                                     top_bottom_data.Country == country].index))  # top_bottom_data.index[top_bottom_data['Country']==country]

    # if country is in top_bottom_data then retreive its order
    if ind != None:
        clickedCountry = int(ind)
    #otherwise find its order in the dataframe containing all countries 
    else:
        country_index = sorted_df[sorted_df.Country == country].index
        top_bottom_data = top_bottom_data.append(sorted_df[sorted_df.Country == country])
        #"numCountry" column contains countries along their order (used for yaxis)
        top_bottom_data.loc[top_bottom_data.Country == country]['numCountry'] = str(country_index + 1) + '.' + \
                                                                                sorted_df.loc[country_index, 'Country'] 

    top_bottom_country = top_bottom_data.sort_index(ascending=False)

    return top_bottom_country, clickedCountry


#get a dictionary for replacing certain vaccination names
def Vaccines(df):
    value = list(df.columns)
    label = pd.Series(value)
    label = label.replace(
        {"Haemoph. influenzae": "Haemophilus influenzae", "Strept. pneumoniae": "Streptococcus pneumoniae",
         "DTP Combination¹": "Diphteria, Tetanus, Pertussis"})
    
    label = label.to_list()
    vaccines = []
    for i in range(0, len(label)):
        vaccines.append(dict(label=label[i], value=value[i]))

    return vaccines


def getDataBarChart():
    return dataBarChart
