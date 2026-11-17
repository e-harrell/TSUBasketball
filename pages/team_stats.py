import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.set_page_config(page_title="Team Statistics", layout="wide")
st.title("Team Statistics")

#read in data
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')

#create  sidebar radio button selector
chart_choice = st.sidebar.radio(
    "Choose a statistic to display:",["Game Points", "Assists", "Rebounds", "Blocks","Steals","Field Goal Percentage", "3-Point Percentage", "Free Throw Percentage"])

#create charts
if chart_choice == "Game Points":
    st.subheader("Game Points")
    df['TSU score'] = df['TSUscore']
    df['Opponent score']=df['Oppscore']
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
    st.altair_chart(chart, width='stretch')
    st.text(f"During the 2025-26 season, the TSU men's basketball team scored an average of {int(np.mean(df['TSU score']))} points per game while their opponent scored an average of {int(np.mean(df['Opponent score']))} points per game. The highest score for TSU was {max(df['TSU score'])} points which occurred on {df.loc[df['TSU score'].idxmax(), 'Date']} against {df.loc[df['TSU score'].idxmax(), 'Opponent']}. The highest score by an opponent was {max(df['Opponent score'])} points which occurred on {df.loc[df['Opponent score'].idxmax(), 'Date']} by {df.loc[df['Opponent score'].idxmax(), 'Opponent']}. TSU's lowest score was {min(df['TSU score'])} points on {df.loc[df['TSU score'].idxmin(), 'Date']} against {df.loc[df['TSU score'].idxmin(), 'Opponent']}. The lowest score of TSU opponents was {min(df['Opponent score'])} points on {df.loc[df['Opponent score'].idxmin(), 'Date']} by {df.loc[df['Opponent score'].idxmin(), 'Opponent']}.")
elif chart_choice == "Assists":
    st.subheader("Assists")
    df['TSU assists'] = df['TSU_AST']
    df['Opponent assists']=df['Opp_AST']
    columns_to_plot = ["TSU assists", "Opponent assists"]
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
            y=alt.Y("Value:Q", title="Assists"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Assists")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
                alt.Tooltip("Value:Q", title="Assists")]))
    st.altair_chart(chart, width='stretch')
    st.text(f"During the 2025-26 season, the TSU men's basketball team had an average of {int(np.mean(df['TSU assists']))} assists per game while their opponent had an average of {int(np.mean(df['Opponent assists']))} assists per game. The highest number of TSU assists was on {df.loc[df['TSU assists'].idxmax(), 'Date']} when {max(df['TSU assists'])} assists were made against {df.loc[df['TSU assists'].idxmax(), 'Opponent']}. The highest number of assists by an opponent was {max(df['Opponent assists'])} assists made on {df.loc[df['Opponent assists'].idxmax(), 'Date']} by {df.loc[df['Opponent assists'].idxmax(), 'Opponent']}. TSU's lowest number of assists in a game was {min(df['TSU assists'])} assists on {df.loc[df['TSU assists'].idxmin(), 'Date']} against {df.loc[df['TSU assists'].idxmin(), 'Opponent']}. The lowest number of assists by TSU opponents was {min(df['Opponent assists'])} assists on {df.loc[df['Opponent assists'].idxmin(), 'Date']} by {df.loc[df['Opponent assists'].idxmin(), 'Opponent']}.")
elif chart_choice == "Rebounds":
    st.subheader("Rebounds")
    df['TSU rebounds'] = df['TSU_RB']
    df['Opponent rebounds']=df['Opp_RB']
    columns_to_plot = ["TSU rebounds", "Opponent rebounds"]
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
            y=alt.Y("Value:Q", title="Rebounds"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Rebounds")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
                alt.Tooltip("Value:Q", title="Rebounds")]))
    st.altair_chart(chart, width='stretch')
    st.text(f"The TSU men's basketball team recovered an average of {int(np.mean(df['TSU rebounds']))} rebounds per game during the 2025-26 season while their opponent recovered an average of {int(np.mean(df['Opponent rebounds']))} rebounds per game. The highest number of rebounds recovered by TSU in a single game was {max(df['TSU rebounds'])} which occurred on {df.loc[df['TSU rebounds'].idxmax(), 'Date']} against {df.loc[df['TSU rebounds'].idxmax(), 'Opponent']}. The highest number of rebounds recovered by an opponent during a game was {max(df['Opponent rebounds'])} rebounds which occurred on {df.loc[df['Opponent rebounds'].idxmax(), 'Date']} by {df.loc[df['Opponent rebounds'].idxmax(), 'Opponent']}. TSU's lowest number of rebounds was {min(df['TSU rebounds'])} rebounds recovered on {df.loc[df['TSU rebounds'].idxmin(), 'Date']} against {df.loc[df['TSU rebounds'].idxmin(), 'Opponent']}. The lowest number of rebounds recovered by TSU opponents in a game was {min(df['Opponent rebounds'])} rebounds on {df.loc[df['Opponent rebounds'].idxmin(), 'Date']} by {df.loc[df['Opponent rebounds'].idxmin(), 'Opponent']}.")
elif chart_choice== "Blocks":
    st.subheader("Blocks") 
    df["TSU blocks"]=df["TSU_BLK"]
    df["Opponent blocks"]=df["Opp_BLK"]
    columns_to_plot = ["TSU blocks", "Opponent blocks"]
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
            y=alt.Y("Value:Q", title="Blocks"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Blocks")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
                alt.Tooltip("Value:Q", title="Blocks")]))
    st.altair_chart(chart, width='stretch')
    st.text(f"The TSU mean's basketball team had an average of {int(np.mean(df['TSU_BLK']))} blocks per game during the 2025-26 season compared to {int(np.mean(df['Opp_BLK']))} blocks per game for their opponents. The game with the highest number of blocks for TSU came on {df.loc[df['TSU_BLK'].idxmax(), 'Date']} when TSU had {max(df['TSU_BLK'])} blocks against {df.loc[df['TSU_BLK'].idxmax(), 'Opponent']}. The highest number of opponent blocks came on {df.loc[df['Opp_BLK'].idxmax(), 'Date']} when {df.loc[df['Opp_BLK'].idxmax(), 'Opponent']} had {max(df['Opp_BLK'])} blocks. The lowest number of TSU blocks occurred on {df.loc[df['TSU_BLK'].idxmin(), 'Date']} when they had {min(df['TSU_BLK'])} blocks against {df.loc[df['TSU_BLK'].idxmin(), 'Opponent']}. The lowest number of blocks committed by a TSU opponent was on {df.loc[df['Opp_BLK'].idxmin(), 'Date']} when {df.loc[df['Opp_BLK'].idxmin(), 'Opponent']} had {min(df['Opp_BLK'])} blocks.")
elif chart_choice == "Steals":
    st.subheader("Steals")
    df['TSU steals'] = df['TSU_STL']
    df['Opponent steals']=df['Opp_STL']
    columns_to_plot = ["TSU steals", "Opponent steals"]
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
            y=alt.Y("Value:Q", title="Steals"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Steals")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
                alt.Tooltip("Value:Q", title="Steals")]))
    st.altair_chart(chart, width='stretch')
    st.text(f"During the 2025-26 season, the TSU men's basketball team had an average of {int(np.mean(df['TSU steals']))} steals per game while their opponent scored an average of {int(np.mean(df['Opponent steals']))} steals per game. The highest number of steals for TSU was {max(df['TSU steals'])} steals which occurred on {df.loc[df['TSU steals'].idxmax(), 'Date']} against {df.loc[df['TSU steals'].idxmax(), 'Opponent']}. The highest number of steals by an opponent was {max(df['Opponent steals'])} steals which occurred on {df.loc[df['Opponent steals'].idxmax(), 'Date']} by {df.loc[df['Opponent steals'].idxmax(), 'Opponent']}. TSU's lowest number of steals was {min(df['TSU steals'])} steals on {df.loc[df['TSU steals'].idxmin(), 'Date']} against {df.loc[df['TSU steals'].idxmin(), 'Opponent']}. The lowest number of steals by TSU opponents was {min(df['Opponent steals'])} steals on {df.loc[df['Opponent steals'].idxmin(), 'Date']} by {df.loc[df['Opponent steals'].idxmin(), 'Opponent']}.")
elif chart_choice == "Field Goal Percentage":
    st.subheader("Field Goal (FG) Percentage")
    df['TSU FG Percentage']=df['TSU_FG_PCT']*100
    df['Opponent FG Percentage']=df['Opp_FG_PCT']*100
    columns_to_plot = ["TSU FG Percentage", "Opponent FG Percentage"]
    custom_colors = ["#171796", "#DC143C"]
    chart = (
        alt.Chart(df)
        .transform_fold(
            columns_to_plot,
            as_=["Metric", "Value"]
        )
        .mark_line(point=True)
        .encode(
            x=alt.X("Date:T", title="Date of Game",),
            y=alt.Y("Value:Q", title="Field Goals Percentage"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Category")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
               alt.Tooltip("Value:Q", title="Value")]))
    st.altair_chart(chart, width='stretch')
    st.write(f"The average field goal percentage for the TSU basketball team during the 2025-26 season was {np.round(np.mean(df['TSU FG Percentage']),1)}% for each game compared to  {np.round(np.mean(df['Opponent FG Percentage']),1)}% for their opponents. TSU's highest field goal percentage came on {df.loc[df['TSU FG Percentage'].idxmax(), 'Date']} when {max(df['TSU FG Percentage'])}% of field goals were made against {df.loc[df['TSU FG Percentage'].idxmax(), 'Opponent']}. TSU's lowest field goal percentage came on {df.loc[df['TSU FG Percentage'].idxmin(), 'Date']} when {min(df['TSU FG Percentage'])}% of field goals were made against {df.loc[df['TSU FG Percentage'].idxmin(), 'Opponent']}. The highest field goal percentage for TSU Opponents was {max(df['Opponent FG Percentage'])}% by {df.loc[df['Opponent FG Percentage'].idxmax(), 'Opponent']} on {df.loc[df['Opponent FG Percentage'].idxmax(), 'Date']}. The lowest field goal percentage by TSU opponents was {min(df["Opponent FG Percentage"])}% by {df.loc[df['Opponent FG Percentage'].idxmin(), "Opponent"]} and occurred on {df.loc[df['Opponent FG Percentage'].idxmin(), 'Date']}.")
elif chart_choice == "3-Point Percentage":
    st.subheader("3-Point Percentage")
    df['TSU 3-Point %']=df['TSU_FG3_PCT']*100
    df['Opponent 3-Point %']=df['Opp_FG3_PCT']*100
    columns_to_plot = ["TSU 3-Point %", "Opponent 3-Point %"]
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
            y=alt.Y("Value:Q", title="3-Point Percentage"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Category")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
               alt.Tooltip("Value:Q", title="Value")]))
    st.altair_chart(chart, width='stretch')
    st.write(f"The average 3-point percentage for the TSU basketball team was {np.round(np.mean(df['TSU 3-Point %']),1)}% for each game during the 2025-26 season compared to {np.round(np.mean(df['Opponent 3-Point %']),1)}% for their opponents. TSU's highest 3-point percentage came on {df.loc[df['TSU 3-Point %'].idxmax(), 'Date']} when {max(df['TSU 3-Point %'])}% of 3 pointers were made against {df.loc[df['TSU 3-Point %'].idxmax(), 'Opponent']}. Their lowest 3-point percentage came on {df.loc[df['TSU 3-Point %'].idxmin(), 'Date']} when {min(df['TSU 3-Point %'])}% of 3-pointers were made against {df.loc[df['TSU 3-Point %'].idxmin(), 'Opponent']}. The opponent with the highest 3-pointer percentage was {df.loc[df["Opponent 3-Point %"].idxmax(), "Opponent"]} who made {max(df["Opponent 3-Point %"])}% of their 3-pointers on {df.loc[df["Opponent 3-Point %"].idxmax(), "Date"]}. The lowest 3-pointer percentage was on {df.loc[df["Opponent 3-Point %"].idxmin(), 'Date']} when {df.loc[df["Opponent 3-Point %"].idxmin(), 'Opponent']} made {min(df["Opponent 3-Point %"])}% of their 3-pointers.")
elif chart_choice == "Free Throw Percentage":
    st.subheader("Free Throw Percentage")
    df['TSU Free Throw %']=df['TSU_FT_PCT']*100
    df['Opponent Free Throw %']=df['Opp_FT_PCT']*100
    columns_to_plot = ["TSU Free Throw %", "Opponent Free Throw %"]
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
            y=alt.Y("Value:Q", title="Free Throw Percentage"),
            color=alt.Color(
                "Metric:N",
                scale=alt.Scale(domain=columns_to_plot, range=custom_colors),
                legend=alt.Legend(title="Category")
            ),
            tooltip=[alt.Tooltip("Date:T", title="Date", format="%b %d, %Y"),
                alt.Tooltip("Metric:N", title="Category"),
               alt.Tooltip("Value:Q", title="Value")]))
    st.altair_chart(chart, width='stretch')
    st.write(f"During the 2025-26 season, the average free throw percentage for the TSU basketball team was {np.round(np.mean(df['TSU Free Throw %']),1)}% for each game compared to {np.round(np.mean(df['Opponent Free Throw %']),1)}% for their opponents. TSU's highest free throw percentage came on {df.loc[df['TSU Free Throw %'].idxmax(), 'Date']} when {np.round(max(df['TSU Free Throw %']),1)}% of free throws were made against {df.loc[df['TSU Free Throw %'].idxmax(), 'Opponent']}. TSU's lowest free throw percentage came on {df.loc[df['TSU Free Throw %'].idxmin(), 'Date']} when {min(df['TSU Free Throw %'])}% of free throws were made against {df.loc[df['TSU Free Throw %'].idxmin(), 'Opponent']}. The highest free throw percentage for TSU opponents was {max(df["Opponent Free Throw %"])}% by {df.loc[df["Opponent Free Throw %"].idxmax(), "Opponent"]} on {df.loc[df["Opponent Free Throw %"].idxmax(), "Date"]}. The lowest free throw percentage by a TSU opponent came on {df.loc[df["Opponent Free Throw %"].idxmin(), 'Date']} where {df.loc[df["Opponent Free Throw %"].idxmin(),"Opponent"]} completed {min(df["Opponent Free Throw %"])}% of their free throws.")