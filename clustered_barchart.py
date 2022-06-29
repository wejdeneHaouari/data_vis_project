'''
This file contains the draw_clusteredBarchart() that plot the mortality rate of children under 5 per refion
For each region the mortality rate is shown for three years (1990,2000,2019)
'''

import plotly.graph_objects as go
import plotly.io as pio
import hover_template

def draw_clusteredBarchart(data):
    fig = go.Figure()
    
    fig.update_layout(
        template=pio.templates['simple_white'],
        dragmode=False,
        #barmode='relative'
    )
  
    colors = ['#630000', "#a80000", '#b8664f']    
    years = ['2019', '2000', '1990']
    for color, year in zip(colors, years):
        fig.add_trace(go.Bar(name=year, x=data[year], y=data['Region'], 
                             orientation='h', marker_color=color,
                             hovertemplate=hover_template.get_clustBarChart_template(year)))
        
    fig.update_layout(barmode='group',
                      legend={'traceorder': 'reversed'},
                      xaxis={'dtick':20, 'title':'Mortality rate per 1000',
                             'title_font_family':'sans-serf'},
                      yaxis={'title_font_family':'sans-serf'},
                      title_text="Mortality Rate of Children under 5 Years Per Region",
                      height=700, width=800, margin_r=10, margin_b=20,
                      margin_pad=4, margin_autoexpand=True
                      )

    return fig
