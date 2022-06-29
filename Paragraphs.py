from dash import html


def descrptionViz1():
    description = [html.P(children=[    
        "The map shows the mortality rate of children under 5 years for each country (The darker the color, the higher the rate). ",
        "For the mortality rate in other age categories, number of death or annual percentage of reduction in the mortality rate, ",
        "please select an option from the drop-down menu. ",
        "For further information, click on a country and a horizontal bar chart will be shown: ",
        "It provide information about the countries with the five highest and five lowest mortality as well as the rank of the clicked country. ",
        "In case of Mortality Rate (under five), a back-to-back chart will also be provided to show mortality per gender." ],
        style={"font-size": "16px"}
    )]
    return description


def ExplainClustBarViz():
    explanation = [html.P(children=[
        "In general, we see that the mortality rate of children under 5 years have been decreasing in all regions since 1990.",
        html.Br(),
        "At a first glance, you see that Western Europen and North America have the lowest mortality rate among all regions. However, North America has a little bit higher mortality rate (8 in 2000 and 6 in 2019) compared to Western Europe (6 in 2000 and 4 in 2019).",
        html.Br(),
        "In addition, West and Central Africa region has the highest mortality rate in all years."],
        style={"font-size": "16px"})
    ]
    return explanation


def descriptionViz4a():
    description = [html.P(children=[
        "Vaccination rates in global regions and the entire world for different vaccines.",
        html.Br(),
        "¹) Combination of vaccines against Diphteria, Tetanus and Pertussis. ",
        html.Br(),
        "²) First dose of vaccine administered. ",
        html.Br(),
        "³) Vaccination at birth."],
        style={"font-size": "16px"})
    ]
    return description


def descriptionViz4b():
    description = [html.P(children=[
        "Distribution of vaccination rate and mortality rate for the selected vaccine for different countries.",
        html.Br(),
        "²) First dose of vaccine administered. ",
        html.Br(),
        "³) Vaccination at birth."],
        style={"font-size": "16px"})
    ]
    return description


def ExplainViz4a():
    explanation = [
        html.P(children=[
            "We see that there are two types of vaccinations that were far less often to be found than others on a ",
            "global scale, namely the vaccines against the rotavirus and streptococcus pneumoniae. ",
            "Also, for North America there is no data available for tuberculosis vaccinations which is surprising. ",
            "As one would expect, less children are fully vaccinated against the measles (two doses) than have had ",
            "just their first dose."],
            style={"font-size": "16px"})
    ]
    return explanation


def InitViz4b():
    initialize = [
        html.P(children=[
            "One might ask whether the vaccination rate influences the mortality rate of the children to such an "
            "extent that it would be obvious from comparing mortality rate and vaccination rate directly. ",
            "This is why the figure on the left shows the mortality rate of children aged 5 to 14 over the vaccination rate. For clarity, just one vaccine is displayed at a time.",
            html.Br(),
            "What do we see? While Niger has the highest mortality rate, it is on average not the country with the "
            "lowest vaccination rates. Nevertheless, most countries with vaccination rates close to 100% are indeed "
            "countries with low child mortalities.",
            html.Br(),
            html.Br(),
            "Please select a vaccine from the dropdown menu to explore the relationships:"],
            style={"font-size": "16px"}),
    ]
    return initialize


def ExplainVis2():
    explanation = [
        html.P(children=[
            "We notice that most of countries the number of death for between 5 and 14 age group is inferior to under "
            "five age  group. To "
            "exploit how mortality rates change with age select a country from the dropdown menu or click on a "
            "marker from the visualization.",
            html.Br()],
            style={"font-size": "16px"})
    ]
    return explanation


def introduction():
    explanation = [
        html.P(children=[
            "According to UNICEF, at least 1 in 3 children under five is under/overweight, and 1 in 2 experience "
            "hidden hunger which lessens the ability of millions of children to grow and develop healthily - leading to "
            "their death. The following charts show mortality and vaccination rates of children around the world.",
            html.Br(),
            "Mortality rate is calculated per 1000 people.",
            html.Br(),
        ],

            style={"font-size": "16px"})
    ]
    return explanation
