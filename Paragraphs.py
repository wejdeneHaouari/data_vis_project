from dash import html

def ExplainClustBarViz():
    explanation = [
        html.P(children=[
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
                          style={"font-size": "12px"})
                   ]
    return description


def descriptionViz4b():
    description = [html.P(children=[
        "Distribution of vaccination rate and mortality rate for the selected vaccine for different countries.",
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
            "We see that there are two types of vaccinations that were far less often to be found than others on a global scale, namely the vaccines against the rotavirus and streptococcus pneumoniae. ",
            "Also, for North America there is no data available for tuberculosis vaccinations which is surprising. ",
            "As one would expect, less children are fully vaccinated against the measles (two doses) than have had just their first dose."],
               style={"font-size": "16px"})
    ]
    return explanation


def InitViz4b():
    initialize = [
        html.P(children=[
            "One might ask whether the vaccination rate influences the mortality rate of the children to such an extent that it would be obvious from comparing mortality rate and vaccination rate directly. ",
            "This is why the figure on the left shows the mortality rate of children aged 5 to 14 over the vaccination rate. For clarity, just one vaccine is displayed at a time.",
            html.Br(),
            "What do we see? While Niger has the highest mortality rate, it is on average not the country with the lowest vaccination rates. Nevertheless, most countries with vaccination rates close to 100% are indeed countries with low child mortalities.",
            html.Br(),
            "Please select a vaccine from the dropdown menu to explore the relationships:"],
               style={"font-size": "16px"}),
    ]
    return initialize

def ExplainVis2():
    explanation = [
        html.P(children=[
            "We can notice that in the majority of the countries most of the deaths are for under five age groups. To "
            "exploit how mortality rates change with age select a country from the dropdown menu or clique on a "
            "marker from the visualization.",
            html.Br()],
               style={"font-size": "16px"})
                    ]
    return explanation