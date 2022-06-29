from dash import html


def generate_table_row(id, style, col1, col2):
    return html.Div(
        id=id,
        className="row table-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                style={"display": "table", "height": "100%"},
                className="two columns row-department",
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"display": "table", "height": "100%"},
                className="two columns row-department",
                children=col2["children"],
            )
        ],
    )
