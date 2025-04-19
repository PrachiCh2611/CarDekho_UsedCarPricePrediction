import streamlit as st

from streamlit_extras.colored_header import colored_header
# At the very top of your script
st.set_page_config(
    page_title="Car Dekho Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)



def app():
    # Custom CSS to adjust the font size of header text
    st.markdown("""
        <style>
            .large-header {
                font-size: 36px;
                font-weight: bold;
            }
            .description {
                font-size: 18px;
                font-style: italic;
            }
        </style>
    """, unsafe_allow_html=True)



# Set background image for the entire page
    st.markdown("""
        <style>
            .stApp {
                background-image: url('C:/Users/HP/OneDrive/Pictures/Screenshots/Screenshot 2025-03-11 194442.png');
                background-size: cover;
                background-position: center center;
                background-repeat: no-repeat;
                width: 120%;                    
                height: 100vh;
            }
        </style>
    """, unsafe_allow_html=True)



 # Custom header text
st.markdown('<p class="large-header">Welcome to CAR DEKHO 👋🏼</p>', unsafe_allow_html=True)
st.markdown('<p class="description">The price prediction is based on Advacned ML Techniques.</p>', unsafe_allow_html=True)






 # Add some visual images or icons for more engagement
st.image("C:/Users/HP/OneDrive/Pictures/Screenshots/Screenshot 2025-03-11 194442.png")
# Run the app
app()
