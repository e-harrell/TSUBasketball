import streamlit as st
import pandas as pd

st.title("Team Statistics")
st.subheader("Statistics for TSU and Opponents for each game of the 2025-26 season")

st.write("Total Game Points")
#read in data
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')

# Plot multiple columns as distinct lines
st.line_chart(
    df,
    x="Date",
    y=["TSUscore", "Oppscore"],
    color=["#171796", "#FCFC2EDA"], x_label='Game Date', y_label='Total Game Points'
)

