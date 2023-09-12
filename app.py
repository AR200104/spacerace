import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


space_race_data = pd.read_csv("data/Space_Corrected.csv")

test_fig = px.bar(space_race_data, x="Rocket", y="Status Mission")

#http://127.0.0.1:8050/
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='test',
        figure=test_fig
    )
])
if __name__ == "__main__":
    app.run(debug=True)