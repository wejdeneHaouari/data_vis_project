'''
This file includes functions to create the bar chart and back-to-back chart
The bar chart shows the mortality rate and rank of the clicked country for the corresponding selected category
Also the top 5 countries (highest mortality) and bottom 5 countries (lowest mortality) are plot 
The bar chart appears when a country clicked on the map
The back-to-back chart shows the same as the bar chart but for separately for male & female
The back-to-back chart appear along the the bar chart only when the selection from the drop-down menu is Mortality Rate (under five)
An empty figure is displayed in place of bar chart and back-to-back chart when above criteria is not met
'''


from re import T
import pandas as pd
import plotly.graph_objects as go
import hover_template
import data 

#create empty figure
def get_empty_figure(chart_type):
    fig = go.Figure()

    #display message depending on chart type
    fig.update_xaxes(showgrid=False, visible=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, visible=False, showticklabels=False)
    if chart_type == 'barchart':
        fig.add_annotation(text="No data to display. Click on a country in the map for more information",
                           showarrow=False)
    else:
        fig.add_annotation(text="No data to display. Click on a country in the map <br> and select Mortality Rate ("
                                "under five) for more information",
                           showarrow=False)
        
    fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", dragmode=False)
    return fig


def draw_barchart(top_bottom_country, columnb, clickedCountry):
    
    colors = ['lightslategray'] * len(top_bottom_country)    #initialize all bars as grey
    colors[clickedCountry] = '#660000'                         #only clicked country bar is red

    fig = go.Figure(data=[
        go.Bar(y=top_bottom_country['numCountry'], x=top_bottom_country[columnb],
               orientation='h', marker_color=colors, base=0,
               hovertemplate= hover_template.get_barChart_template()
               )
    ])

    fig.update_layout(barmode='stack',
                      showlegend=False,
                      xaxis={"title_text": data.get_selected_group_label(columnb, top_bottom_country.copy())},
                      hoverlabel=dict(bgcolor='white', font_size=16),
                      height=420, width=620, 
                      margin_r=50, margin_b=50, margin_l=50, 
                      margin_pad=4, margin_autoexpand=True)

    return fig



def draw_b2bchart(top_bottom_country, clickedCountry):
    '''
    since there is no direct option to draw back-to-back chart 
        a horizontal bar chart is drawn where 
        male is plot on positive xaxis and female on negative xaxis 
    in order to avoid displaying negative data for female:
        for the tooltip, customdata is used and data read directly from column (instead of %{x})
        for the xaxis ticks, negative ticks converted to positive 
    '''
    colors = ['lightslategray'] * len(top_bottom_country)     #initialize all bars as grey
    colors[clickedCountry] = '#660000'                        #only clicked country bar is red

    fig = go.Figure(data=[
        go.Bar(y=top_bottom_country['numCountry'], x=top_bottom_country['Under-five mortality rate 2019, male'],
               orientation='h', name="Male", marker_color=colors, base=0,
               hovertemplate= hover_template.get_b2bChart_template('Male')
               ),
        go.Bar(y=top_bottom_country['numCountry'], x=-top_bottom_country['Under-five mortality rate 2019, Female'],
               orientation='h', name="Female", marker_color=colors, base=0,
               customdata=top_bottom_country['Under-five mortality rate 2019, Female'],
               hovertemplate=hover_template.get_b2bChart_template('Female')
               )
               ])

    fig.layout.xaxis.range = [-140, 140]
    stepSize = 20
    r = range(fig.layout["xaxis"]["range"][0], fig.layout["xaxis"]["range"][1], stepSize)
    fig.update_layout(barmode='stack',
                      showlegend=False,
                      xaxis={"tickvals": list(r),
                             "ticktext": [t if t >= 0 else -t for t in r],  # to convert negative ticks of Female
                             "title_text": 'Female Mortality Rate  vs. Male Mortality Rate'},
                      hoverlabel=dict(bgcolor='white', font_size=16),
                      height=420, width=620, 
                      margin_r=50, margin_b=50, margin_l=50, 
                      margin_pad=4, margin_autoexpand=True
                      )

    return fig
