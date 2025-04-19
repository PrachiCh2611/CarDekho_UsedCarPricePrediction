import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="CarDekho Data Analysis", layout="wide")

def app():
    colored_header(
        label='\U0001F4CA You are on the Data :green[Analysis] Page',
        color_name='green-70',
        description='Explore trends in car prices based on various attributes.'
    )

    @st.cache_data
    def load_data():
        return pd.read_csv('Cleaned_Car_Dheko.csv')

    df = load_data()

    # Section: Price vs Feature
    with st.container():
        st.subheader("\U0001F4C8 Car Price vs Selected Feature")
        choice = st.selectbox("Choose a feature to compare with Car Price:", df.drop('Car_Price', axis=1).columns)
        fig = px.histogram(df, x=choice, y='Car_Price', width=1000, height=450, color_discrete_sequence=['#16a085'])
        st.plotly_chart(fig)

    # Section: Car Brand Availability
    with st.container():
        st.subheader("\U0001F3C6 Most Available Car Brands")
        brand = df.groupby('Manufactured_By').count().reset_index()[['Manufactured_By', 'Fuel_Type']]
        fig = px.bar(brand, x='Manufactured_By', y='Fuel_Type', width=1000, height=450,
                     labels={'Fuel_Type': 'Total Count'}, color_discrete_sequence=['#2980b9'])
        st.plotly_chart(fig)

    # Section: Highest Priced Car Models
    with st.container():
        st.subheader("\U0001F4B8 Highest Priced Car Models")
        top_models = df.sort_values('Car_Price', ascending=False).head(60)
        filtered = top_models[~top_models['Manufactured_By'].isin(['Maruti', 'Chevrolet', 'Hyundai', 'Honda', 'Tata'])]
        fig = px.bar(filtered, x='Car_Model', y='Car_Price', color='Car_Price', width=1000, height=450,
                     color_continuous_scale='hot', hover_name='Manufactured_By',
                     hover_data=['Car_Produced_Year', 'Kilometers_Driven', 'No_of_Owners'])
        st.plotly_chart(fig)

    # Section: Lowest Priced Car Models
    with st.container():
        st.subheader("\U0001F4B5 Lowest Priced Car Models")
        low_models = df.sort_values('Car_Price').head(60)
        filtered = low_models[~low_models['Manufactured_By'].isin(['BMW', 'Land Rover', 'Mercedes-Benz'])]
        fig = px.bar(filtered, x='Car_Model', y='Car_Price', color='Car_Price', width=1000, height=450,
                     color_continuous_scale='turbo', hover_name='Manufactured_By',
                     hover_data=['Car_Produced_Year', 'Kilometers_Driven', 'No_of_Owners'])
        st.plotly_chart(fig)

    # Section: Brand & Model Specific Analysis
    with st.container():
        st.subheader("\U0001F50D Detailed Brand & Model Insights")
        col1, col2 = st.columns(2)

        with col1:
            selected_brand = st.selectbox("Choose a Car Brand:", df['Manufactured_By'].unique())
            brand_data = df[df['Manufactured_By'] == selected_brand]

        with col2:
            selected_model = st.selectbox("Choose a Car Model:", brand_data['Car_Model'].unique())

        model_stats = brand_data.groupby(['Car_Model', 'Car_Produced_Year'])['Car_Price'].mean().reset_index()
        specific_model = model_stats[model_stats['Car_Model'] == selected_model]

        fig = px.bar(specific_model, x='Car_Produced_Year', y='Car_Price', color='Car_Price',
                     color_continuous_scale='rainbow', width=1000, height=450, hover_name='Car_Model')
        st.plotly_chart(fig)

    # Section: Kilometers Driven vs Price
    with st.container():
        st.subheader("\U0001F698 Kilometers Driven vs Car Price")
        scatter = px.scatter(brand_data, x='Kilometers_Driven', y='Car_Price', color='Car_Model',
                             size='Car_Price', hover_name='Manufactured_By',
                             hover_data=['Car_Model', 'Fuel_Type', 'Car_Produced_Year',
                                         'Transmission_Type', 'Mileage(kmpl)', 'No_of_Seats', 'Engine_CC'],
                             width=1000, height=450)
        st.plotly_chart(scatter)

    # Section: Mileage vs Price
    with st.container():
        st.subheader("\u26FD Mileage vs Car Price")
        scatter = px.scatter(brand_data, x='Mileage(kmpl)', y='Car_Price', color='Car_Model',
                             size='Car_Price', hover_name='Manufactured_By',
                             hover_data=['Car_Model', 'Fuel_Type', 'Car_Produced_Year',
                                         'Transmission_Type', 'Kilometers_Driven', 'No_of_Seats', 'Engine_CC'],
                             width=1000, height=450)
        st.plotly_chart(scatter)

    # Section: Car Age vs Price
    with st.container():
        st.subheader("\U0001F552 Car Age vs Car Price")
        scatter = px.scatter(brand_data, x='Car_Age', y='Car_Price', color='Car_Model',
                             size='Car_Price', hover_name='Manufactured_By',
                             hover_data=['Car_Model', 'Fuel_Type', 'Car_Produced_Year',
                                         'Transmission_Type', 'Kilometers_Driven', 'Mileage(kmpl)', 'No_of_Seats', 'Engine_CC'],
                             width=1000, height=450)
        st.plotly_chart(scatter)

    # Section: Central Tendency by Location
    with st.container():
        st.subheader("\U0001F4CD Location-wise Price Insights")
        col1, col2 = st.columns(2)

        with col1:
            selected_location = st.radio("Select Location:", options=df['Location'].unique(), horizontal=True)

        with col2:
            selected_stat = st.selectbox("Select Central Tendency:", ['mean', 'median', 'mode'])

        filtered_data = df[(df['Manufactured_By'] == selected_brand) & (df['Location'] == selected_location)]

        if selected_stat == 'mean':
            result = filtered_data.groupby(['Manufactured_By', 'Car_Model'])['Car_Price'].mean().reset_index()
        elif selected_stat == 'median':
            result = filtered_data.groupby(['Manufactured_By', 'Car_Model'])['Car_Price'].median().reset_index()
        else:  # mode
            result = filtered_data.groupby(['Manufactured_By', 'Car_Model'])['Car_Price'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None).reset_index()

        fig = px.pie(result, names='Car_Model', values='Car_Price', width=950, height=450,
                     hover_name='Manufactured_By', hole=0.3)
        st.plotly_chart(fig)

# Run the app function
app()
