import streamlit as st


def home():
    st.set_page_config(page_title="Cycling Analytics Platform", layout="wide", page_icon="🚴")

    st.title("🚴 Cycling Analytics Platform")
    st.markdown(
        "<p style='font-size:18px; color:grey;'>A suite of tools for understanding cycling patterns in Flanders.</p>",
        unsafe_allow_html=True,
    )
    st.divider()

    cards = [
        {
            "icon": "🌤️",
            "title": "Weather Simulation",
            "desc": "Predict cyclist counts at Flemish monitoring sites based on weather conditions and time of day. Adjust sliders to simulate different scenarios.",
            "url": "weather",
        },
        {
            "icon": "🚴",
            "title": "Cycling Timelapse",
            "desc": "Watch an animated map of real cyclist traffic flow across Flanders. See which sites are busiest hour by hour throughout the day.",
            "url": "timelapse",
        },
        {
            "icon": "⚠️",
            "title": "Accident Risk",
            "desc": "Explore the GTRI accident risk model. Identify high-risk sites based on weather, traffic volume, and temporal patterns across Flanders.",
            "url": "accident-risk",
        },
        {
            "icon": "🔵",
            "title": "Cluster Analysis",
            "desc": "Explore clustering of Flemish cycling monitoring sites based on traffic patterns and site characteristics.",
            "url": "clusters",
        },
        # {
        #     "icon": "📊",
        #     "title": "Circulation Plan Analysis",
        #     "desc": "Compare observed cyclist counts against a weather-normalised baseline before and after circulation plan changes in Aalst and Kortrijk.",
        #     "url": "circulation",
        # },
    ]

    card_html = (
        "<style>"
        ".card-grid{display:flex;gap:1rem;}"
        ".card-link{flex:1;text-decoration:none!important;color:inherit;}"
        ".card-link:hover .card-box{border-color:#aaa;background:#f7f7f7;}"
        ".card-box{border:1px solid #e0e0e0;border-radius:0.5rem;padding:1rem;height:100%;box-sizing:border-box;transition:border-color 0.15s,background 0.15s;cursor:pointer;}"
        ".card-icon{font-size:1.8rem;line-height:1;margin-bottom:0.4rem;}"
        ".card-title{font-weight:700;font-size:1rem;margin-bottom:0.4rem;}"
        ".card-desc{font-size:0.85rem;color:#666;margin:0;}"
        "</style>"
        '<div class="card-grid">'
    )
    for card in cards:
        card_html += (
            f'<a class="card-link" href="{card["url"]}" target="_self">'
            f'<div class="card-box">'
            f'<div class="card-icon">{card["icon"]}</div>'
            f'<div class="card-title">{card["title"]}</div>'
            f'<p class="card-desc">{card["desc"]}</p>'
            f'</div></a>'
        )
    card_html += "</div>"
    st.markdown(card_html, unsafe_allow_html=True)

    st.divider()
    


pg = st.navigation([
    st.Page(home, title="Home", icon="🏠", default=True),
    st.Page("weather_model/weather_hub.py",           title="Weather Simulation",       icon="🌤️", url_path="weather"),
    st.Page("timelapse_tool/timelapse_app.py",        title="Cycling Timelapse",        icon="🚴",  url_path="timelapse"),
    st.Page("accident_model/07_GTRI_dashboard.py",    title="Accident Risk",            icon="⚠️",  url_path="accident-risk"),
    st.Page("model_cluster/app.py",                   title="Cluster Analysis",         icon="🔵",  url_path="clusters"),
    # st.Page("weather_model/case_study.py",            title="Circulation Plan Analysis",icon="📊",  url_path="circulation"),
])
pg.run()
