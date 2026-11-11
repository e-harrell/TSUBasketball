import pandas as pd
import streamlit as st
import numpy as np

# Create a map dataset with coordinates
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')
mapdata=df[['Date','Opponent', 'Opponent_Latitude', 'Opponent_Longitude']]

# create distinct coordinates with jittering to keep from having the exact same coordinates 
# for 2 different games in the same city

jitter_amount = 0.0005

mapdata["latitude"] = mapdata["Opponent_Latitude"] + np.random.normal(0, jitter_amount, size=len(mapdata))
mapdata["longitude"] = mapdata["Opponent_Longitude"] + np.random.normal(0, jitter_amount, size=len(mapdata))

st.title("Game Locations")
st.text("Map of Game Locations for the  2025-26 Season")

# 2. Add the selection box
selected_game = st.selectbox(
    "Choose a game to display on the map:", options=df["Date"].unique()
)

# 3. Filter the dataframe based on the selection
filtered_df = mapdata[mapdata["Date"] == selected_game]

# 4. Display game information metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("Latitude", filtered_df["latitude"].values[0])
with col2:
    st.metric("Longitude", filtered_df["longitude"].values[0])

# 5. Render the filtered point on the map
# st.map automatically reads 'lat' and 'lon' columns to center and zoom
st.map(filtered_df, zoom=10)
