'''
    Contains some functions to preprocess the data used in the visualisation.
'''
from numpy import NaN
import pandas as pd


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
    # print(label)
    label = label.replace({"Under-five_mortality_rate_2019,both": "Mortality rate (under five)",
                            "Neonatal mortality rate 2019": "Mortality rate (Neonatal)",
                            "Infant mortality rate 2019": "Mortality rate (Infant)",
                            "Mortality rate among children aged 5–14 years, 2019": "Mortality rate (5-14 years)",
                            "Annual rate of reduction in under-five mortality rate\t": "Annual percentage of reduction for mortality rate (under five)",
                            "Annual rate of reduction in stillbirth rate": "Annual percentage of reduction for mortality rate (stillbirth)",
                            "Under five deaths 2019": "Number of deaths (under five)",
                            "Deaths among children aged 5–14 years 2019": "Number of deaths (5-14 years)"})
    # print(label)
    label = label.to_list()
    variables = []
    for i in range(0, len(label)):
        variables.append(dict(label=label[i], value=value[i]))   
    return variables



def get_selected_group(selectedGroup):
    print(selectedGroup)
    columns_dict={"Under-five_mortality_rate_2019,both": "Mortality rate (under five)", 
                            "Neonatal mortality rate 2019": "Mortality rate (Neonatal)",
                            "Infant mortality rate 2019": "Mortality rate (Infant)",
                            "Mortality rate among children aged 5–14 years, 2019": "Mortality rate (5-14 years)",
                            "Annual rate of reduction in under-five mortality rate\t": "Annual percentage of reduction for mortality rate (under five)",
                            "Annual rate of reduction in stillbirth rate": "Annual percentage of reduction for mortality rate (stillbirth)",
                            "Under five deaths 2019": "Number of deaths (under five)",
                            "Deaths among children aged 5–14 years 2019": "Number of deaths (5-14 years)"
                            }
    columnb=columns_dict[selectedGroup]
    print(columnb)
    return columnb

def top_bottom(my_df, columnb):

    my_df=my_df.dropna(axis=0)

    my_df['Under-five mortality rate 2019, male']=my_df['Under-five mortality rate 2019, male'].astype(int)
    my_df['Under-five mortality rate 2019, Female']=my_df['Under-five mortality rate 2019, Female'].astype(int)
    
    my_df[columnb]=pd.to_numeric(my_df[columnb])#my_df[column].astype(int)

    sorted_df=my_df.sort_values(by=[columnb], ascending=False, ignore_index=True)

    sorted_df=sorted_df[['Country',columnb,'Under-five mortality rate 2019, male','Under-five mortality rate 2019, Female']]
    sorted_df['numCountry']=""
    
    for index,row in sorted_df.iterrows():
        sorted_df.loc[index,'numCountry'] = str(index+1)+'.'+ sorted_df.loc[index,'Country'] 
    
    top=sorted_df.iloc[-5:,:]
    top_bottom_data=top.append(sorted_df.iloc[0:5,:])
        
    top_bottom_data=top_bottom_data.sort_index(ascending =False) 
    
    return sorted_df, top_bottom_data



