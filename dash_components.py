from dash import dcc
from dash import html
import scatterplot


def generate_country_dropdown(countries):
    return html.Div(
        id="country_dropdown_vis2",
        children=[
            dcc.Dropdown(countries, id='country-select', placeholder="Select Country"),
            html.Br(),
            html.Div(id='dd-output-container')
        ],
    )


def generate_vis2(dataframe):
    fig = scatterplot.add_scatter_matrix(dataframe)
    return html.Div(
        id="vis2",
        children=[
            dcc.Graph(figure=fig, id='graph',
                      config=dict(
                          showTips=False,
                          showAxisDragHandles=False,
                          displayModeBar=False))
        ],
    )


def generate_info_panel2():
    table = html.Div(

        style={'visibility': 'hidden'},
        id="info-panel-vis2",
        children=[
            html.Table([
                html.Tr(children=[html.Td(id='group1'), html.Td(id='rate1')], style={"color": "red"}),
                html.Tr([html.Td(id='group2'), html.Td(id='rate2')]),
                html.Tr([html.Td(id='group3'), html.Td(id='rate3')]),
                html.Tr([html.Td(id='group4'), html.Td(id='rate4')]),
                html.Tr([html.Td(id='group5'), html.Td(id='rate5')]),
            ]),
        ])
    return table
