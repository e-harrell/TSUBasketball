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
#rename coordinate columns so that streamlit can recognize them & columns can be used in for loop below
df_dash=df_dash.rename(columns={"Game_Latitude":"lat", "Game_Longitude": "lon", 
                                "TSUscore": "TSU_score", "Oppscore": "Opp_score"})

#Add the selection box (dropdown menu)
selected_date = st.selectbox(
    "Choose a game date to display game statistics and location:", df_dash["Date"])

#Create filtered data based on dropdown
selected_row=df_dash[df_dash['Date'] == selected_date]

#generate container for Side-by-side map and table
with st.container(border=True):
    map_col, table_col_1, table_col_2, table_col_3 = st.columns([3, 2,2,2])

#generate map
with map_col:
    st.subheader("Map of Game Location")
    if selected_row.empty:
        st.info("No games match the selected filter.")
    else:
        st.map(selected_row, latitude="lat", longitude="lon", size="visitors")

#generate game statistics table
Labels_list=['Team', 'Score', 'Assists', 'Rebounds', 'Blocks', 'Steals', 'Field Goal %', '3-point %', 'Free Throw %']
selected_row['TSU_FG_PCT']=np.round(selected_row['TSU_FG_PCT']*100,1)
selected_row['Opp_FG_PCT']=np.round(selected_row['Opp_FG_PCT']*100,1)
selected_row['TSU_FG3_PCT']=np.round(selected_row['TSU_FG3_PCT']*100,1)
selected_row['Opp_FG3_PCT']=np.round(selected_row['Opp_FG3_PCT']*100,1)
selected_row['TSU_FT_PCT']=np.round(selected_row['TSU_FT_PCT']*100,1)
selected_row['Opp_FT_PCT']=np.round(selected_row['Opp_FT_PCT']*100,1)
TSU_list=["Tennessee State University"]
Opp_list=["Opponent"]
for col in selected_row.columns:
    if 'TSU_' in col:
        TSU_list.extend(selected_row[col].tolist()) 
    elif 'Opp_' in col:
        Opp_list.extend(selected_row[col].tolist())
    else:
        continue

with table_col_1:
    for element in Labels_list:
        st.text(element)
with table_col_2:
    for element in TSU_list:
        st.text(element)
with table_col_3:
    for element in Opp_list:
        st.text(element)
    





