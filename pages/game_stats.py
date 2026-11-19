import pandas as pd
import streamlit as st
import numpy as np

#Page title 
st.title("Game Statistics and Map")

#Read in dataset 
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')
#filter dataset to get only needed columns
df_dash=df[['Date', "Opponent",'Game_Latitude','Game_Longitude', "TSUscore", "Oppscore", "TSU_AST", "Opp_AST", 
            "TSU_RB", "Opp_RB", "TSU_BLK", "Opp_BLK", "TSU_STL", "Opp_STL", "TSU_FG_PCT", "Opp_FG_PCT",
            "TSU_FG3_PCT", "Opp_FG3_PCT", "TSU_FT_PCT","Opp_FT_PCT"]]
#rename coordinate columns so that streamlit can recognize them
df_dash=df_dash.rename(columns={"Game_Latitude":"lat", "Game_Longitude": "lon"})

#Add the selection box (dropdown menu)
selected_date = st.selectbox(
    "Choose a game date to display game statistics and location:", df_dash["Date"])

#Create filtered data based on dropdown
selected_row=df_dash[df_dash['Date'] == selected_date]

#generate container for Side-by-side map and table
with st.container(border=True):
    map_col, table_col = st.columns([3, 7])

#generate map
with map_col:
    st.subheader("Map of Game Location")
    if selected_row.empty:
        st.info("No games match the selected filter.")
    else:
        st.map(selected_row, latitude="lat", longitude="lon", size="visitors")

#generate game statistics table
#rename columns for game statistics
selected_row=selected_row.rename(columns={
"TSUscore": "TSU Score",
"Oppscore": "Opponent Score",
"TSU_AST": "TSU Assists",
"Opp_AST": "Opponent Assists",
"TSU_RB": "TSU Rebounds",
"Opp_RB": "Opponent Rebounds",
"TSU_BLK": "TSU Blocks",
"Opp_BLK": "Opponent Blocks",
"TSU_STL" :"TSU Steals",
"Opp_STL" :"Opponent Steals",
"TSU_FG_PCT": "TSU Field Goal %",
"Opp_FG_PCT": "Opponent Gield Goal %",
"TSU_FG3_PCT": "TSU 3-Pointer %",
"Opp_FG3_PCT" : "Opponent 3-Pointer %",
"TSU_FT_PCT" :"TSU Free Throw %",
"Opp_FT_PCT": "Opponent Free Throw %"})
#getting correct format for %s
selected_row["TSU Field Goal %"]=np.round(selected_row["TSU Field Goal %"]*100,1)
selected_row["Opponent Gield Goal %"]=np.round(selected_row["Opponent Gield Goal %"]*100,1)
selected_row["TSU 3-Pointer %"]=np.round(selected_row["TSU 3-Pointer %"]*100,1)
selected_row["Opponent 3-Pointer %"]=np.round(selected_row["Opponent 3-Pointer %"]*100,1)
selected_row["TSU Free Throw %"]=np.round(selected_row["TSU Free Throw %"]*100,1)
selected_row["Opponent Free Throw %"]=np.round(selected_row["Opponent Free Throw %"]*100,1)
selected_row_transposed=selected_row.T
with table_col:
    st.subheader("Game Statistics")
    st.table(selected_row_transposed)





