import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

country_replacement = {"Gran Canaria": "Spain", "New Mexico": "USA", "Shahrud Missile Test Site": "Iran", "Pacific Missile Range Facility": 'USA'}

test_race = pd.read_csv("data/Space_Corrected.csv")
test_race["Country"] = test_race["Location"].str.split(", ").str[-1]
space_race_data = test_race
#grouped_comp = test_race["Company Name"].value_counts()#.sort_values(ascending=False)
#grouped_comp = pd.DataFrame(grouped_comp)
grouped_comp = test_race.groupby("Company Name").size().sort_values(ascending=False).reset_index(name="Count")
company_df = pd.DataFrame(grouped_comp)
company_df.columns=["Company", "Count"]
#grouped_comp = grouped_comp.rename(columns={'Company Name': 'Count'})
#figure = px.
active_inactive = test_race["Status Rocket"].value_counts().reset_index(name="count")
print(type(space_race_data.replace(country_replacement)))
print(active_inactive.columns)

cost_bar_df = space_race_data["Rocket"].value_counts().reset_index(name="count")
print(cost_bar_df.columns)
cost_bar = px.bar(cost_bar_df, x="Rocket", y="count")
print(cost_bar_df.sort_values("Rocket"))
country_starts = space_race_data.groupby("Country").size().sort_values(ascending=False).reset_index(name="Count")
country_starts = pd.DataFrame(country_starts)
country_starts.columns = ["Country", "Count"]
starts_per_country = country_starts
#Add alpha3 country codes


#starts_per_country = country_starts
#Add alpha3 country codes
alpha3_codes = {"Russia": "RUS", "Kazakhstan": "KAZ", "France": "FRA", "China": "CHN", "Japan": "JAP",\
               "India": "IND", "Kiribati": "KIR", "Iran": "IRA", "New Zealand": "NZL", "Israel": "ISR", \
                "Kenya": "KEN", "Australia": "AUS", "North Korea": "PRK", "South Korea": "KOR",\
               "Brazil": "BRA", "Spain": "ESP"}
region_replacement = {"Yellow Sea": "China", "Barents Sea": "Russia"}
#starts_per_country["Code"] = starts_per_country["Country"]
#starts_per_country["Code"].replace(alpha3_codes, inplace=True)
#print(starts_per_country)
starts_per_country = space_race_data.replace(region_replacement)

starts_per_country = starts_per_country.groupby("Country").size().sort_values(ascending=False).reset_index(name="Count")
starts_per_country = pd.DataFrame(starts_per_country)
starts_per_country.columns=["Country", "Count"]
starts_per_country["Code"] = starts_per_country["Country"]
starts_per_country["Code"].replace(alpha3_codes, inplace=True)


starts_map = go.Choropleth(locations=starts_per_country["Code"], z=starts_per_country["Count"], text=starts_per_country["Country"], \
                           colorscale="Blues", marker_line_color="gray", marker_line_width=0.2)
starts_map_fig = go.Figure(data=starts_map)
starts_map_fig.update_layout(geo=dict(
                            showframe=False,
                            showcoastlines=False,
                            projection_type='equirectangular'),
                            width=1200,
                            height=600
                            )
starts_map_fig.show()
print(starts_per_country)
go.Box()