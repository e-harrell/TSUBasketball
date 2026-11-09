import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("What a Year!")
st.header("An Analysis of the 2025-26 season of the Tennessee State University Men's Basketball Team")
st.subheader("This is the subheader")
st.markdown("This is the markdown")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.subheader("2025-2026 Season Statistics")

# Define the relative path to your file
data = "TSUdata.csv"

try:
    # Load and display the file
    df = pd.read_csv(data)
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"Could not find the file at {data}. Please check your file path.")

# map of locations of all teams that TSU played
#get subset of data
dfmap1=df[['Opponent', 'Opponent_Latitude', 'Opponent_Longitude']]
#rename coordinate columns so that streamlit will pick them up:
dfmap1=dfmap1.rename(columns={"Opponent_Latitude": "lat", "Opponent_Longitude": "lon"}, inplace=True)
#create streamlit map
st.map(dfmap1)

