from re import T
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import preprocess



def get_empty_figure(chart_type):
    
    fig = go.Figure()
    fig.update_xaxes(showgrid=False, visible=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, visible=False, showticklabels=False)
    if chart_type=='barchart':
        fig.add_annotation(text="No data to display. Click on a country in the map for more information",
                       showarrow=False)
    else:
        fig.add_annotation(text="No data to display. Click on a country in the map and select Mortality Rate (under five) for more information",
                       showarrow=False)
    fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", dragmode=False)
    return fig



def insert_country(sorted_df, top_bottom_data, country):
    
    #default order for country if not one of the top 5 or bottom 5
    clickedCountry=5

    ind=top_bottom_data.index.get_indexer_for((top_bottom_data[top_bottom_data.Country==country].index))#top_bottom_data.index[top_bottom_data['Country']==country]
  
    #if country is not in top_bottom_data then retreive its order 
    if ind != None:
        clickedCountry = int(ind)
    #otherwise find its order in the top_bottom_data
    else:
        country_index=sorted_df[sorted_df.Country==country].index
        top_bottom_data=top_bottom_data.append(sorted_df[sorted_df.Country==country])
        top_bottom_data.loc[top_bottom_data.Country==country]['numCountry'] = str(country_index+1)+'.'+ sorted_df.loc[country_index,'Country']     

    top_bottom_country = top_bottom_data.sort_index(ascending =False)  
    
    return top_bottom_country, clickedCountry



def draw_barchart(top_bottom_country, columnb, clickedCountry):
    
  
    colors = ['lightslategray',] * 11
    colors[clickedCountry] = '#660000'
    
    fig = go.Figure(data=[
        go.Bar(y=top_bottom_country['numCountry'], x=top_bottom_country[columnb], 
               orientation='h', marker_color=colors, base=0, 
               hovertemplate='<b>Country</b> : %{y}<br><b>Mortality Rate</b> : %{x}<extra></extra>'
   )
    ])

    
    fig.update_layout(barmode='stack',
                      title={'text': '',
                             'x':0.5,
                             'xanchor': 'center',
                            },
                      showlegend = False,
                      xaxis={"title_text": preprocess.get_selected_group(columnb)},
                      hoverlabel=dict(bgcolor='white',font_size=16),
                      height=420, width=620, margin_r=10, margin_b=20, margin_pad=4, margin_autoexpand=True)

    #fig.update_yaxes(categoryorder='array', categoryarray=top_bottom['Country'], title_standoff= 1)

    return fig



def draw_b2bchart(top_bottom_country, clickedCountry):
    
    colors = ['lightslategray'] * 11
    colors[clickedCountry] = '#660000'
    pd.set_option('display.max_columns', None)

    fig = go.Figure(data=[
        go.Bar(y=top_bottom_country['numCountry'], x=top_bottom_country['Under-five mortality rate 2019, male'], 
               orientation='h', name="Male", marker_color=colors, base=0, 
               hovertemplate='<b>Country</b> : %{y}<br><b>Male Mortality Rate</b> : %{x}<extra></extra>'
            ),
        go.Bar(y=top_bottom_country['numCountry'], x=-top_bottom_country['Under-five mortality rate 2019, Female'], 
               orientation='h', name="Female",marker_color=colors, base=0,customdata=top_bottom_country['Under-five mortality rate 2019, Female'],
                hovertemplate='<b>Country</b> : %{y}<br><b>Female Mortality Rate</b> : %{customdata}<extra></extra>')
        ])

    
    
    fig.layout.xaxis.range = [-140, 140] 
    stepSize = 20
    r = range(fig.layout["xaxis"]["range"][0], fig.layout["xaxis"]["range"][1], stepSize)
    fig.update_layout(barmode='stack',
                      title={'text': "Mortality Rate of Children Under 5 Years",
                             'x':0.5,
                             'xanchor': 'center',
                            },
                      showlegend = False,
                      xaxis={"tickvals":list(r),
                             "ticktext":[t if t>=0 else -t for t in r],
                             "title_text": 'Female Mortality Rate  vs. Male Mortality Rate',
                            },
                      hoverlabel=dict(bgcolor='white',font_size=16),
                      height=420, width=620, margin_r=10, margin_b=20, margin_pad=4, margin_autoexpand=True
                    )
    
    return fig
