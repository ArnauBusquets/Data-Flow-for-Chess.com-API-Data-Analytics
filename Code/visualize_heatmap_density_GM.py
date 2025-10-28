

#Sort this dict by the amount of times that each country appears (the value of each key)
diction = {'Olympic': 2, 'China': 43, 'Russia': 118, 'Serbia': 37, 'Latvia': 8, 'United States': 219, 'Portugal': 5, 'Egypt': 4, 'Brazil': 19, 'Azerbaijan': 26, 'Iran': 16, 'Uzbekistan': 15, 'India': 102, 'Poland': 45, 'Canada': 20, 'Palestine': 2, 'Colombia': 9, 'Estonia': 3, 'Jordan': 1, 'Qatar': 5, 'United Kingdom': 27, 'Belarus': 7, 'International': 34, 'Ukraine': 62, 'Czech Republic': 18, 'North Macedonia': 5, 'Spain': 55, 'Israel': 25, 'Argentina': 22, 'Algeria': 1, 'Kazakhstan': 18, 'Denmark': 8, 'Romania': 20, 'Peru': 10, 'Tunisia': 1, 'Monaco': 2, 'Uruguay': 2, 'Japan': 7, 'Netherlands': 38, 'France': 54, 'Norway': 23, 'Australia': 11, 'Slovenia': 10, 'Armenia': 28, 'Thailand': 2, 'Greenland': 2, 'Cuba': 18, 'British Virgin Islands': 1, 'Germany': 53, 'Montenegro': 4, 'Saint Kitts/Nevis': 3, 'Croatia': 18, 'Sweden': 17, 'Turkmenistan': 5, 'Hungary': 37, 'Austria': 13, 'The Gambia': 1, 'Iceland': 13, 'England': 17, 'Mongolia': 9, 'Georgia': 23, 'North Korea': 3, 'Philippines': 15, 'Tanzania': 2, 'United Arab Emirates': 6, 'Türkiye': 22, 'Indonesia': 5, 'Bermuda': 1, 'Slovakia': 7, 'Haiti': 1, 'Singapore': 4, 'Vietnam': 12, 'Saint Lucia': 1, 'Switzerland': 15, 'Togo': 1, 'Bulgaria': 20, 'South Africa': 2, 'Bosnia-Herzegovina': 3, 'Paraguay': 5, 'Tuvalu': 2, 'Lithuania': 7, 'Belgium': 5, 'Greece': 13, 'Chinese Taipei': 1, 'Italy': 14, 'Ireland': 2, 'Saudi Arabia': 1, 'Tajikistan': 1, 'Hong Kong': 1, 'Jamaica': 1, 'Isle of Man': 2, 'Ivory Coast': 1, 'Scotland': 3, 'Ecuador': 1, 'Malaysia': 1, 'Senegal': 1, 'Moldova': 6, 'Tonga': 1, 'Chile': 4, 'Cayman Islands': 2, 'Dominican Republic': 2, 'Taiwan': 1, 'Mexico': 6, 'Saint Vincent and the Grenadines': 1, 'European Union': 2, 'Barbados': 1, 'Antigua/Barbuda': 1, 'Bolivia': 1, 'Guatemala': 1, 'Namibia': 1, 'Marshall Islands': 1, 'Micronesia': 1, 'Bangladesh': 3, 'Panama': 1, 'Andorra': 1, 'Uganda': 1, 'Liechtenstein': 1, 'Turks and Caicos Islands': 1, 'American Samoa': 1, 'Catalonia': 1, 'South Korea': 1, 'El Salvador': 1, 'Finland': 1, 'Somalia': 1, 'US Virgin Islands': 1, 'Ghana': 1, 'Maldives': 2, 'Central Africa': 1, 'Brunei': 1, 'Vatican City': 1, 'Gibraltar': 1}
# sorted_dict = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dict)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


df = pd.DataFrame(list(diction.items()), columns=["country", "value"])
# Eliminar entradas que no son países reconocidos
invalids = ["Olympic", "International", "European Union", "Catalonia", "England", "Scotland"]
df = df[~df["country"].isin(invalids)]

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="value",
    hover_name="country",
    color_continuous_scale="Blues",
    range_color=(0, df["value"].quantile(0.95))  # ignora el top 5%
)

# Añadir los números como texto encima de cada país
fig.add_trace(go.Scattergeo(
    locations=df["country"],
    locationmode="country names",
    text=df["value"],
    mode="text",
    textfont=dict(color="black", size=10),
    showlegend=False
))

fig.update_layout(
    title="Density of GM per country",
    geo=dict(showframe=False, showcoastlines=True)
)

fig.show()