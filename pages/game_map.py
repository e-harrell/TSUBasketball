import pandas as pd
import streamlit as st

# Create a dataset with coordinates
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')
mapdata=df[['Date','Opponent', 'Game_Latitude', 'Game_Longitude', 'Game_Location']]
mapdata=mapdata.rename(columns={'Game_Latitude': 'lat', 'Game_Longitude': 'lon'})

st.title("Game Locations")

st.markdown(
    """
    <style>
    div[data-testid="stSelectbox"] label p {
        font-size: 24px !important;
        font-weight: bold; /* Optional: make it stand out more */
    }
    </style>
    <style>
    div[data-testid="stMetric"] label p {
        font-size: 24px !important;
       
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Add the selection box (dropdown menu)
selected_game = st.selectbox(
    "Choose a game date to display game location on the map:", options=mapdata["Date"].unique())

# Create filtered data based on dropdown
selected_row=mapdata[mapdata['Date'] == selected_game]

# Define two columns for our metrics
col1, col2 = st.columns(2)
with col1:
    st.metric(label='Opponent',value=selected_row['Opponent'].values[0])
with col2:
    st.metric(label='Location',value=selected_row['Game_Location'].values[0])

#Disaply map
st.map(selected_row, zoom=10)




