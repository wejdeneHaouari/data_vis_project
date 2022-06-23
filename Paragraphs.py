from dash import html
from dash import dcc


def descriptionViz4a():
    description = [html.P(children=[
        "Left: Vaccination rates in global regions and the entire world for different vaccines. Right: Distribution of vaccination rate and mortality rate for the selected vaccine.",
        html.Br(),
        "¹) Combination of vaccines against Diphteria, Tetanus and Pertussis. ",
        html.Br(),
        "²) First dose of vaccine administered. ",
        html.Br(),
        "³) Vaccination at birth."],
                          style={"font-size": "12px"})
                   ]
    return description


def ExplainViz4a():
    explanation = [
        html.P(children=[
            "We see that there are two types of vaccines that were far less often administered in 2019 than others on a global scale, namely the vaccines against the rotavirus and streptococcus pneumoniae. ",
            "Also, for North America there is no data available for tuberculosis vaccinations which is surprising. ",
            "As one would expect, less children are fully vaccinated against the measles (two doses) than have had just their first dose."],
               style={"font-size": "16px"})
    ]

    return explanation


def InitViz4b():
    initialize = [
        html.P(children=[
            "One might ask whether the vaccination rate influences the mortality rate of the children to such an extent that it would be obvious from comparing mortality rate and vaccination rate directly. ",
            "This is why the next figure shows the mortality rate of children aged 5 to 14 over the vaccination rate. For clarity, just one vaccine is displayed at a time. ",
            html.Br(),
            "Please select a vaccine from the dropdown menu to explore the relationships:"],
               style={"font-size": "16px"}),
    ]

    return initialize
