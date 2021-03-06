'''
    This file contains the code for the choropleth map.
'''

import plotly.express as px
import hover_template
import data


def get_map(my_df, variable, VarList):
    '''
        Generates the choropleth map.
        Args:
            my_df: The dataframe to display
        Returns:
            The generated figure
    '''
    variable_to_print = data.getName(variable, VarList)
    fig = px.choropleth(my_df, locations="country_code",
                        color=variable,
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Reds)
    fig.update_traces(hovertemplate=hover_template.get_map_template(),
                      customdata=my_df["Country"])
    fig.update_layout(title_text=variable_to_print,
                      geo=dict(showframe=True,
                               showcoastlines=False,
                               projection_type='equirectangular'))
    fig.update_layout(margin={"r": 40, "t": 40, "l": 40, "b": 40})
    return fig
