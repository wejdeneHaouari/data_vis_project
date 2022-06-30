import plotly.express as px
import hover_template
import data


def getHeatmap(data):
    XLabels = ["<b>"+x+"</b>" for x in data.columns]
    fig = px.imshow(data, labels=dict(color="Vaccination rate (%)"),
                    x=data.columns, y=data.index, zmin=0, zmax=100)
    fig.update_layout(dragmode=False)
    fig.update_layout(height=420, width=620, margin_r=10, margin_b=20, 
                      title="Vaccinations per region", title_x=0, title_y=1)
    fig.update_layout(xaxis_title=None, yaxis_title=None, margin_pad=4,
                      margin_autoexpand=True, plot_bgcolor="white")
    fig.update_layout(coloraxis=dict(
        colorbar=dict(bgcolor="white",
                      len=1,
                      tick0=0,
                      dtick=25,
                      ypad=0,
                      xpad=0,
                      showticklabels=True,
                      ticklen=5,
                      tickcolor="darkgrey",
                      tickmode="linear",
                      ticks="outside",
                      title=dict(side="right",
                                 text="<b>Vaccination rate (%)</b>",
                                 font=dict(family="Arial Rounded MT Bold, sans-serif",
                                           size=18))),
        colorscale=[[0.0, "#dddce7"], [0.00005, "#630000"],
                    [0.4, "#a80000"], [1.0, "#fff8f6"]])) 
    fig.update_xaxes(side="top", ticks="outside", tickangle=-40,
                     tickmode="array", tickvals=data.columns,
                     automargin=True, showgrid=True, ticktext=XLabels,
                     tickfont=dict(size=14, family="Arial Rounded MT Bold, sans-serif"))
    fig.update_yaxes(side="left", tickangle=0, automargin=True, 
                     showgrid=True, tickfont_size=14)
    custom = fig["data"][0]["z"].tolist()
    custom = [["No data available" if x == -5
               else str(x)+" %" for x in a] for a in custom]
    fig.update_traces(hovertemplate=hover_template.get_heatmap_template(),
                      customdata=custom)
    return fig


def initScatter(data, Vacc, VaccList):
    data = data.reset_index()
    fig = px.scatter(data,
                     x="Mortality rate among children aged 5–14 years, 2019", y=Vacc)
    fig.update_layout(height=370, width=620,
                      margin=dict(l=20, b=10, r=30),
                      plot_bgcolor="lightgrey",
                      coloraxis_colorbar=None, 
                      coloraxis_showscale=False,
                      title="Vaccination and children's mortality per country", title_x=0, title_y=1)
    fig.update_yaxes(title_text="Vaccination rate (%)",
                     range=[0.0, 100.0],
                     dtick=25,
                     showgrid=True,
                     gridcolor="darkgrey",
                     showticklabels=True,
                     showticksuffix="all",
                     ticksuffix=" ",
                     ticks="outside",
                     ticklen=5,
                     tickcolor="darkgrey") 
    fig.update_xaxes(title_text="mortality rate of children aged 5 to 14 (per 1000)",
                     title_font_family="Arial",
                     title_font_size=14,
                     side="top",
                     range=[0.0, 35.0],
                     automargin=True,
                     title_standoff=0,
                     gridcolor="darkgrey",
                     dtick=10)
    fig.update_traces(hovertemplate=hover_template.get_scatter_template(),
                      customdata=data["Countries"])
    fig.update_traces(marker_color="#630000", marker_size=10,
                      marker_opacity=0.7)
    fig = AnnotateVaccineName(fig, Vacc, VaccList)
    return fig


def AnnotateVaccineName(figure, Vacc, VaccList):
    figure.update_layout(annotations=[dict(
        x=0.995,
        y=0.01,
        bgcolor="white",
        height=25,
        bordercolor="#630000",
        align="right",
        valign="bottom",
        text="<b>" + data.getName(Vacc, VaccList) + "</b>",
        font=dict(family="Arial Rounded MT Bold, sans-serif", size=18, color="black"),
        showarrow=False,
        xref="paper",
        yref="paper",
        xanchor="right",
        yanchor="bottom",
        textangle=0
    )])
    return figure
