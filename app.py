import streamlit as st

# 1. Define individual pages
home_page = st.Page(
    page="pages/home.py", 
    title="Home", 
    icon=":material/home:", 
    default=True
)
game_map_page = st.Page(
    page="pages/game_map.py", 
    title="Game Locations", 
    icon=":material/map:"
)
opponent_map_page = st.Page(
    page="pages/opponent_map.py", 
    title="Opponent Locations", 
    icon=":material/map:"
)
tsu_stats_page = st.Page(
    page="pages/tsu_stats.py", 
    title="2025-26 TSU Statistics", 
    icon=":material/trending_up:"
)
opponent_stats_page = st.Page(
    page="pages/opponent_stats.py", 
    title="2025-26 Opponent Statistics", 
    icon=":material/trending_up:"
)
statistical_analysis_page = st.Page(
    page="pages/statistical_analysis.py", 
    title="Statistical Analysis of TSU and Opponent Data", 
    icon=":material/analytics:"
)
# 2. Group into dashboard sections
navigation_menu = st.navigation({
    "Pages": [home_page,game_map_page, opponent_map_page, tsu_stats_page, opponent_stats_page, statistical_analysis_page]
})

# 3. Apply global page configs and execute navigation
st.set_page_config(page_title="2025-26 TSU Basketball Analysis", layout="wide")
navigation_menu.run()
