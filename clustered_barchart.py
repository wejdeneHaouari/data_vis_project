import plotly.graph_objects as go
import plotly.io as pio


def draw_barchart(data):
    fig = go.Figure()
    fig.update_layout(
        template=pio.templates['simple_white'],
        dragmode=False,
        barmode='relative',
        # title="Mortality Rate of Children Under 5 Years"

    )

    # print(data.columns)

    colors = ['#630000', "#a80000",'#b8664f']  # ['#202020','#4f4f4f','#9e9e9e']  "
    years = ['2019', '2000', '1990']
    for color, year in zip(colors, years):
        fig.add_trace(go.Bar(name=year, x=data[year], y=data['Region'], orientation='h', marker_color=color,
                             hovertemplate='<b>Region</b> : %{y}<br><b>Year</b> : ' + year + '<br><b>Mortality Rate</b> : %{x}<extra></extra>'
                             ))

    # print(list(data['Region']))

    fig.update_layout(barmode='group',
                      yaxis=dict(categoryorder='array',
                                 categoryarray=data['Region']),

                      legend={'traceorder': 'reversed'},
                      xaxis=dict(dtick=20, title="Mortality rate per 1000"),
                      title_text="Mortality Rate of Children under 5 Years Per Region",
                      # yaxis = dict(autorange='reversed')

                      )

    return fig
