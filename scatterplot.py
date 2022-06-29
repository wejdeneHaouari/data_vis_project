import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import hover_template as hover


def add_scatter_matrix(data):
    fig = make_subplots(rows=1, cols=5,
                        subplot_titles=("Stillbirth", "Neonatal", "Infant", "Under-five", "Between 5-14 "))
    # stillbirth
    fig.add_trace(
        go.Scatter(
            text="stillbirth",
            y=data['stillbirth'],
            mode='markers',
            marker=dict(color='#aaaaaa'),
            customdata=data['country'],
            hovertemplate=hover.vis2Hover()),
        row=1, col=1
    )
    fig['layout']['xaxis'].update(visible=False)
    fig['layout']['yaxis'].update(range=[0, 120])
    # neonatal
    fig.add_trace(
        go.Scatter(text="Neonatal",
                   y=data['neonatal'],
                   mode='markers',
                   marker=dict(color='#aaaaaa'),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()

                   ),
        row=1, col=2
    )
    fig['layout']['xaxis2'].update(visible=False)
    fig['layout']['yaxis2'].update(range=[0, 120])

    # Infant
    fig.add_trace(
        go.Scatter(text="Infant",
                   y=data['infant'],
                   mode='markers',
                   marker=dict(color='#aaaaaa'),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=3
    )
    fig['layout']['xaxis3'].update(visible=False)
    fig['layout']['yaxis3'].update(range=[0, 120])

    # Under-five
    fig.add_trace(
        go.Scatter(text="Under five",
                   y=data['under-five'],
                   mode='markers',
                   marker=dict(color='#aaaaaa'),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=4
    )
    fig['layout']['xaxis4'].update(visible=False)
    fig['layout']['yaxis4'].update(range=[0, 120])

    fig.add_trace(
        go.Scatter(text="Between 4 and 14",
                   y=data['between 5-14'],
                   mode='markers',
                   marker=dict(color='#aaaaaa'),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=5
    )
    fig['layout']['xaxis5'].update(visible=False)
    fig['layout']['yaxis5'].update(range=[0, 120])

    fig.update_layout(height=600,
                      width=1100,
                      title_text="Mortality Rate per group age",
                      showlegend=False
                      )

    return fig


def update_vis2(data, country):
    # get index where country = country
    index_country = data.index[data['country'] == country].tolist()[0]
    colors = ['#aaaaaa'] * len(data)
    opacity = [0.5] * len(data)
    colors[index_country] = 'red'
    opacity[index_country] = 1
    fig = make_subplots(rows=1, cols=5,
                        subplot_titles=("Stillbirth", "Neonatal", "Infant", "Under-five", "Between 5-14 "))
    # stillbirth
    fig.add_trace(
        go.Scatter(
            text="stillbirth",
            y=data['stillbirth'],
            mode='markers',
            marker=dict(color=colors, opacity=opacity),
            customdata=data['country'],
            hovertemplate=hover.vis2Hover()),
        row=1, col=1
    )
    fig['layout']['xaxis'].update(visible=False)
    fig['layout']['yaxis'].update(range=[0, 120])
    # neonatal
    fig.add_trace(
        go.Scatter(text="Neonatal",
                   y=data['neonatal'],
                   mode='markers',
                   marker=dict(color=colors,opacity=opacity),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()

                   ),
        row=1, col=2
    )
    fig['layout']['xaxis2'].update(visible=False)
    fig['layout']['yaxis2'].update(range=[0, 120])

    # Infant
    fig.add_trace(
        go.Scatter(text="Infant",
                   y=data['infant'],
                   mode='markers',
                   marker=dict(color=colors, opacity=opacity),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=3
    )
    fig['layout']['xaxis3'].update(visible=False)
    fig['layout']['yaxis3'].update(range=[0, 120])

    # Under-five
    fig.add_trace(
        go.Scatter(text="Under five",
                   y=data['under-five'],
                   mode='markers',
                   marker=dict(color=colors, opacity=opacity),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=4
    )
    fig['layout']['xaxis4'].update(visible=False)
    fig['layout']['yaxis4'].update(range=[0, 120])

    fig.add_trace(
        go.Scatter(text="Between 4 and 14",
                   y=data['between 5-14'],
                   mode='markers',
                   marker=dict(color=colors,opacity=opacity),
                   customdata=data['country'],
                   hovertemplate=hover.vis2Hover()),
        row=1, col=5
    )
    fig['layout']['xaxis5'].update(visible=False)
    fig['layout']['yaxis5'].update(range=[0, 120])

    fig.update_layout(height=600,
                      width=1100,
                      title_text="Mortality Rate per group age",
                      showlegend=False
                      )

    return fig
