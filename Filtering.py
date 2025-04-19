import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import plotly.express as px
import io


def app():
    colored_header(
        label='🔍 APPLY :blue[Filters]',
        color_name='blue-70',
        description='Filter CarDekho Cars Based on Your Preferences'
    )

    @st.cache_data
    def load_data():
        df = pd.read_csv('Cleaned_Car_Dheko.csv')
        return df

    df = load_data()

    # Ensure year columns are strings
    df['Car_Produced_Year'] = df['Car_Produced_Year'].astype(str)
    df['Registration_Year'] = df['Registration_Year'].astype(str)

    # Sidebar Exploration
    st.sidebar.markdown("### 🔎 Explore Unique Values")
    choice = st.sidebar.selectbox("Select a column to view unique values:", options=['Car_Model', 'Manufactured_By'])
    if choice == 'Car_Model':
        unique_values_df = pd.DataFrame({'Car Models': df['Car_Model'].unique()})
    else:
        unique_values_df = pd.DataFrame({'Car Companies': df['Manufactured_By'].unique()})
    st.sidebar.dataframe(unique_values_df, use_container_width=True)

    # Filters with Dataframe Explorer
    st.markdown("### 🧮 Filter the Car Dataset")
    filter_df = dataframe_explorer(df, case=False)

    submit = st.button("🎯 Apply Filters", use_container_width=True)

    if submit:
        st.markdown("### 📋 Filtered Results")
        st.dataframe(filter_df, use_container_width=True, hide_index=True)
        st.success(f"🔢 {len(filter_df)} cars matched your filter criteria.")

        # Download options
        csv = filter_df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Filtered Data as CSV", data=csv, file_name="filtered_cars.csv", mime='text/csv', use_container_width=True)

        # Basic Visualization
        if len(filter_df) > 0:
            st.markdown("### 📊 Quick Visualizations")
            with st.expander("🔹 Car Price by Model"):
                fig1 = px.bar(filter_df.groupby('Car_Model')['Car_Price'].mean().reset_index().sort_values('Car_Price', ascending=False),
                              x='Car_Model', y='Car_Price',
                              title='Average Car Price by Model',
                              color='Car_Price', color_continuous_scale='Blues')
                st.plotly_chart(fig1, use_container_width=True)

            with st.expander("🔹 Car Price vs Year"):
                fig2 = px.scatter(filter_df, x='Car_Produced_Year', y='Car_Price',
                                 color='Car_Model', title='Car Price vs Produced Year')
                st.plotly_chart(fig2, use_container_width=True)

            with st.expander("🔹 Car Price by Location"):
                fig3 = px.box(filter_df, x='Location', y='Car_Price', points="all",
                              title='Car Price Distribution by Location')
                st.plotly_chart(fig3, use_container_width=True)

        # Optional: Add a little animation for flair
        rain(emoji="🚗", font_size=30, falling_speed=5, animation_length="medium")
