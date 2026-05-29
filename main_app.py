import streamlit as st


def home():
    st.set_page_config(page_title="Cycling Analytics Platform", layout="wide", page_icon="🚴")

    st.title("🚴 Cycling Analytics Platform")
    st.markdown(
        "<p style='font-size:18px; color:grey;'>A suite of tools for understanding cycling patterns in Flanders.</p>",
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown("""
    <style>
    [data-testid="stPageLink"] a {
        font-weight: 700;
        font-size: 1rem;
        text-decoration: none !important;
    }
    [data-testid="stPageLink"] p { margin-bottom: 0; }
    </style>
    """, unsafe_allow_html=True)

    cards = [
        {
            "icon": "🌤️",
            "title": "Weather Simulation",
            "desc": "Predict cyclist counts at Flemish monitoring sites based on weather conditions and time of day. Adjust sliders to simulate different scenarios.",
            "page": "weather_model/weather_hub.py",
        },
        {
            "icon": "🚴",
            "title": "Cycling Timelapse",
            "desc": "Watch an animated map of real cyclist traffic flow across Flanders. See which sites are busiest hour by hour throughout the day.",
            "page": "timelapse_tool/timelapse_app.py",
        },
        {
            "icon": "⚠️",
            "title": "Accident Risk",
            "desc": "Explore the GTRI accident risk model. Identify high-risk sites based on weather, traffic volume, and temporal patterns across Flanders.",
            "page": "accident_model/07_GTRI_dashboard.py",
        },
        {
            "icon": "🔵",
            "title": "Cluster Analysis",
            "desc": "Explore clustering of Flemish cycling monitoring sites based on traffic patterns and site characteristics.",
            "page": "model_cluster/app.py",
        },
        {
            "icon": "📊",
            "title": "Circulation Plan Analysis",
            "desc": "Compare observed cyclist counts against a weather-normalised baseline before and after circulation plan changes in Aalst and Kortrijk.",
            "page": "weather_model/case_study.py",
        },
    ]

    cols = st.columns(len(cards))
    for col, card in zip(cols, cards):
        with col:
            with st.container(border=True):
                st.markdown(f"<div style='font-size:1.8rem;line-height:1;margin-bottom:0.3rem'>{card['icon']}</div>", unsafe_allow_html=True)
                st.page_link(card["page"], label=card["title"])
                st.caption(card["desc"])

    st.divider()
    


pg = st.navigation([
    st.Page(home, title="Home", icon="🏠", default=True),
    st.Page("weather_model/weather_hub.py",           title="Weather Simulation",       icon="🌤️", url_path="weather"),
    st.Page("timelapse_tool/timelapse_app.py",        title="Cycling Timelapse",        icon="🚴",  url_path="timelapse"),
    st.Page("accident_model/07_GTRI_dashboard.py",    title="Accident Risk",            icon="⚠️",  url_path="accident-risk"),
    st.Page("model_cluster/app.py",                   title="Cluster Analysis",         icon="🔵",  url_path="clusters"),
    st.Page("weather_model/case_study.py",            title="Circulation Plan Analysis",icon="📊",  url_path="circulation"),
])
pg.run()
