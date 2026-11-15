import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.set_page_config(page_title="Game Statistics", layout="wide")
st.title("Game Statistics")

#read in data
df = pd.read_csv(r'C:\Users\E_A_H\OneDrive\Desktop\data science projects\TSUbasketball\TSUdata.csv')

