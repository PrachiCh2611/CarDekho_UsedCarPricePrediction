import streamlit as st
from streamlit_option_menu import option_menu
import Home, Filtering, Analysis, Prediction
from PIL import Image

# Load logo for main page (not sidebar)
img = Image.open("C:/Users/HP/OneDrive/Pictures/Screenshots/Screenshot 2025-03-11 194442.png")

st.set_page_config(
    page_title="Used Car Price Predictor 🚗",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="auto"
)

# Display logo and app title
col1, col2 = st.columns([1, 5])
with col1:
    st.image(img, width=80)
with col2:
    st.markdown("## Welcome to CARDEKHO🚗 **Used Car Price Predictor**")

# Welcome note with interactivity hint
st.markdown("""
<div style='text-align: center; font-size: 17px; color: #444;'>Analyze, filter, and predict used car prices with ease. Start by choosing a feature from the sidebar!</div>
""", unsafe_allow_html=True)

# Add an expandable section for tips
with st.expander("💡 Tips to Use This App"):
    st.markdown("""
    - Navigate between pages using the **sidebar menu**.
    - Use sliders and dropdowns for filtering and predictions.
    - In **Analysis**, explore charts and summaries.
    - Head to **Prediction** to try out price prediction in real-time!
    """)

# Class to handle multiple apps
class multiapp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({'title': title, 'function': function})

    def run(self):
        with st.sidebar:
            st.markdown("### 🔍 Navigate")
            app = option_menu(
                menu_title="Used Car Price Prediction",
                options=["Home", "Data Filtering", "Data Analysis", "Data Prediction"],
                icons=['house', 'filter-circle', 'bar-chart-line', 'graph-up-arrow'],
                menu_icon='car-front-fill',
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#A95C68"},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {
                        "font-size": "18px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#C4A484"
                    },
                    "nav-link-selected": {"background-color": "#C04000"},
                }
            )

        # Loading animation when switching tabs
        with st.spinner("Loading your selection..."):
            if app == 'Home':
                Home.app()
            elif app == 'Data Filtering':
                Filtering.app()
            elif app == 'Data Analysis':
                Analysis.app()
            elif app == 'Data Prediction':
                Prediction.app()

# Initialize app
app = multiapp()
app.add_app("Home", Home.app)
app.add_app("Data Filtering", Filtering.app)
app.add_app("Data Analysis", Analysis.app)
app.add_app("Data Prediction", Prediction.app)

# Run the multi-page app
app.run()

# Sticky help tip at the bottom
st.markdown("---")
st.markdown("<center>💬 Need help? Use the tips above !</center>", unsafe_allow_html=True)
