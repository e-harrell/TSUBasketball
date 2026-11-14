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
        x=alt.X("Date:T", title="Date of Game"),
        y=alt.Y("Value:Q", title="Total Game Points"),
        color=alt.Color(
            "Metric:N",
            scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
            legend=alt.Legend(title="Scores")
        ),
        tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
            alt.Tooltip("Metric:N", title="Category"),
            alt.Tooltip("Value:Q", title="Game Points")]))
st.altair_chart(chart, use_container_width=True)
st.text(f"During the 2025-26 season, the TSU men's backetball team scored an average of {int(np.mean(df['TSU score']))} points per game while their opponent scored an average of {int(np.mean(df['Opponent score']))} points per game. The highest score for TSU was {max(df['TSU score'])} points which occurred on {df.loc[df['TSU score'].idxmax(), 'Date']} against {df.loc[df['TSU score'].idxmax(), 'Opponent']}. The highest score by an opponent was {max(df['Opponent score'])} points which occurred on {df.loc[df['Opponent score'].idxmax(), 'Date']} by {df.loc[df['Opponent score'].idxmax(), 'Opponent']}. TSU's lowest score was {min(df['TSU score'])} points on {df.loc[df['TSU score'].idxmin(), 'Date']} against {df.loc[df['TSU score'].idxmin(), 'Opponent']}. The lowest score of TSU opponents was {min(df['Opponent score'])} points on {df.loc[df['Opponent score'].idxmin(), 'Date']} by {df.loc[df['Opponent score'].idxmin(), 'Opponent']}.")

st.subheader("Field Goals (FG) Attempted and Made")
df['TSU FG Made']=df['TSU_FGM']
df['TSU FG Attempts']=df['TSU_FGA']
df['Opponent FG Made']=df['Opp_FGM'] 
df['Opponent FG Attempts']=df['Opp_FGA']
columns_to_plot = ["TSU FG Made", "Opponent FG Made", "TSU FG Attempts", "Opponent FG Attempts"]
custom_colors = ["#171796", "#DC143C", "#ADD8E6", "#800020"]
chart = (
    alt.Chart(df)
    .transform_fold(
        columns_to_plot,
        as_=["Metric", "Value"]
    )
    .mark_line(point=True)
    .encode(
        x=alt.X("Date:T", title="Date of Game"),
        y=alt.Y("Value:Q", title="Number of Field Goals Attempted & Made"),
        color=alt.Color(
            "Metric:N",
            scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
            legend=alt.Legend(title="Category")
        ),
        tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
            alt.Tooltip("Metric:N", title="Category"),
            alt.Tooltip("Value:Q", title="Value")]))
st.altair_chart(chart, use_container_width=True)
st.write(f"TSU had an average of {int(np.mean(df['TSU FG Attempts']))} field goal attempts per game during the 2025-26 season while their opponents had an average of {int(np.mean(df['Opponent FG Attempts']))} attempts per game. TSU's greatest number of attempts came on {df.loc[df['TSU FG Attempts'].idxmax(), 'Date']} when {max(df['TSU FG Attempts'])} attempts were made against {df.loc[df['TSU FG Attempts'].idxmax(), 'Opponent']}. Their lowest number of attempts came on {df.loc[df['TSU FG Attempts'].idxmin(), 'Date']} when {min(df['TSU FG Attempts'])} attempts were made against {df.loc[df['TSU FG Attempts'].idxmin(), 'Opponent']}.")
st.write(f"TSU made an average of {int(np.mean(df['TSU FG Made']))} field goals per game during the 2025-26 season while their opponents made an average of {int(np.mean(df['Opponent FG Made']))} field goals per game. TSU had the most field goals on {df.loc[df['TSU FG Made'].idxmax(), 'Date']} when {max(df['TSU FG Made'])} were made against {df.loc[df['TSU FG Made'].idxmax(), 'Opponent']}. The least number of field goals came on {df.loc[df['TSU FG Made'].idxmin(), 'Date']} when {min(df['TSU FG Made'])} field goals were made against {df.loc[df['TSU FG Made'].idxmin(), 'Opponent']}.")