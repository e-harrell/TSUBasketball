import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
#read in data
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')
df['TSU score'] = df['TSUscore']
df['Opponent score']=df['Oppscore']
st.title("Team Statistics")
st.subheader("Statistics for TSU and Opponents for each game of the 2025-26 season")

st.subheader("Total Game Points")
columns_to_plot = ["TSU score", "Opponent score"]
custom_colors = ["#171796", "#DC143C"]
chart = (
    alt.Chart(df)
    .transform_fold(
        columns_to_plot,
        as_=["Metric", "Value"]
    )
    .mark_line(point=True)
    .encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Value:Q", title="Total Game Points"),
        color=alt.Color(
            "Metric:N",
            scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
            legend=alt.Legend(title="Team")
        ),
        tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
            alt.Tooltip("Metric:N", title="Team"),
            alt.Tooltip("Value:Q", title="Game Points")]))
st.altair_chart(chart, use_container_width=True)
st.write(f"During the 2025-26 season, the TSU men's backetball team scored an average of {int(np.mean(df['TSU score']))} points per game while their opponent scored an average of {int(np.mean(df['Opponent score']))} points per game.")
st.write(f"The highest score for TSU was {max(df['TSU score'])} points which occurred on {df.loc[df['TSU score'].idxmax(), 'Date']} against {df.loc[df['TSU score'].idxmax(), 'Opponent']}.")
st.write(f"The highest score by an opponent was {max(df['Opponent score'])} points which occurred on {df.loc[df['Opponent score'].idxmax(), 'Date']} by {df.loc[df['Opponent score'].idxmax(), 'Opponent']}.")
st.write(f"TSU's lowest score was {min(df['TSU score'])} points on {df.loc[df['TSU score'].idxmin(), 'Date']} against {df.loc[df['TSU score'].idxmin(), 'Opponent']}.")
st.write(f"The lowest score of TSU opponents was {min(df['Opponent score'])} points on {df.loc[df['Opponent score'].idxmin(), 'Date']} by {df.loc[df['Opponent score'].idxmin(), 'Opponent']}.")