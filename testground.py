import pandas as pd
import plotly.express as px


test_race = pd.read_csv("data/Space_Corrected.csv")
test_race["Country"] = test_race["Location"].str.split(", ").str[-1]
#grouped_comp = test_race["Company Name"].value_counts()#.sort_values(ascending=False)
#grouped_comp = pd.DataFrame(grouped_comp)
grouped_comp = test_race.groupby("Company Name").size().sort_values(ascending=False).reset_index(name="Count")
company_df = pd.DataFrame(grouped_comp)
company_df.columns=["Company", "Count"]
#grouped_comp = grouped_comp.rename(columns={'Company Name': 'Count'})
#figure = px.

print(test_race)
