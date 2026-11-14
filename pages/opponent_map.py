import pandas as pd
import pydeck as pdk
import streamlit as st
import numpy as np

#  Prepare your data
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')
mapdata=df[['Opponent', 'Opponent_Latitude', 'Opponent_Longitude']]

# create distinct coordinates with jittering to keep from having the exact same coordinates 
# for 2 different schools in the same city

jitter_amount = 0.0005

mapdata["latitude"] = mapdata["Opponent_Latitude"] + np.random.normal(0, jitter_amount, size=len(mapdata))
mapdata["longitude"] = mapdata["Opponent_Longitude"] + np.random.normal(0, jitter_amount, size=len(mapdata))


#  Create a Pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=mapdata,
    get_position=["longitude", "latitude"],
    get_radius=15000,
    get_color=[23, 23, 150],
    pickable=True,  # Required for tooltips to work
   )

# 3. Define the view state
view_state = pdk.ViewState(latitude=39.8283, longitude=-98.5795, zoom=3.5)

# 4. Configure the tooltip and render the chart
deck = pdk.Deck(map_style='road',
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{Opponent}"},  # Use \n for new lines
)
st.title("Opponent Map")
st.write("Locations of Opponents for the 2025-26 Season")
st.pydeck_chart(deck)

