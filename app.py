import streamlit as st
st.set_page_config(layout="wide")
# 1. Define individual pages
home_page = st.Page(
    page="pages/home.py", 
    title="Home", 
    icon=":material/home:", 
    default=True
)
opponent_map_page = st.Page(
    page="pages/opponent_map.py", 
    title="Opponent Locations", 
    icon=":material/map:"
)
game_stats_page = st.Page(
    page="pages/game_stats.py", 
    title="Game Statistics", 
    icon=":material/trending_up:"
)
team_stats_page = st.Page(
    page="pages/team_stats.py", 
    title="Team Statistics", 
    icon=":material/trending_up:"
)
statistical_analysis_page = st.Page(
    page="pages/statistical_analysis.py", 
    title="Statistical Analysis", 
    icon=":material/analytics:"
)
# 2. Group into dashboard sections
navigation_menu = st.navigation({
    "Menu": [home_page, opponent_map_page, team_stats_page, game_stats_page,  statistical_analysis_page]
})

navigation_menu.run()
