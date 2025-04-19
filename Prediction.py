import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import pandas as pd
import pickle

def app():
    colored_header(
        label='🚗 Welcome to Data :red[Prediction] Page',
        color_name='red-70',
        description='CarDekho Used Cars Price Prediction 💰'
    )

    @st.cache_data
    def load_data():
        df = pd.read_csv('Cleaned_Car_Dheko.csv')
        df1 = pd.read_csv('Preprocessed_Car_Dheko.csv')
        return df, df1

    df, df1 = load_data()

    # Drop irrelevant columns
    drop_cols = ['Manufactured_By', 'No_of_Seats', 'No_of_Owners', 'Fuel_Type', 'Registration_Year', 'Car_Age']
    df.drop(drop_cols, axis=1, inplace=True)
    df1.drop(drop_cols, axis=1, inplace=True)

    # Encode categorical columns
    for col in df.columns:
        if df[col].dtype == 'object':
            decode = df[col].sort_values().unique()
            encode = df1[col].sort_values().unique()
            globals()[col] = dict(zip(decode, encode))

    # 🎯 Prediction Form
    with st.form(key='prediction_form', clear_on_submit=False):
        st.subheader("🔧 Car Details")

        car_model = st.selectbox("🚙 Select a Car Model", options=df['Car_Model'].unique())
        model_year = st.selectbox("📅 Select Car Production Year", options=df['Car_Produced_Year'].unique())
        transmission = st.radio("🔄 Transmission Type", options=df['Transmission_Type'].unique(), horizontal=True)
        location = st.selectbox("📍 Select Location", options=df['Location'].unique())

        st.subheader("📈 Performance Metrics")

        km_driven = st.number_input(
            f"🛣️ Kilometers Driven (Min: {df['Kilometers_Driven'].min()}, Max: {df['Kilometers_Driven'].max()})",
            min_value=0.0, value=10000.0
        )

        engine_cc = st.number_input(
            f"🛠️ Engine CC (Min: {df['Engine_CC'].min()}, Max: {df['Engine_CC'].max()})",
            min_value=0.0, value=1200.0
        )

        mileage = st.number_input(
            f"⛽ Mileage (kmpl) (Min: {df['Mileage(kmpl)'].min()}, Max: {df['Mileage(kmpl)'].max()})",
            min_value=0.0, value=18.0
        )

        def inv_trans(x):
            return 0 if x == 0 else 1 / x

        with open('GradientBoost_model.pkl', 'rb') as file:
            model = pickle.load(file)

        predict_btn = st.form_submit_button('🔍 Predict Price', use_container_width=True)

        if predict_btn:
            prediction = model.predict([[
                inv_trans(km_driven),
                Transmission_Type[transmission],
                Car_Model[car_model],
                model_year,
                engine_cc,
                mileage,
                Location[location]
            ]])
            st.success(f"💸 **Predicted Car Price: ₹ {prediction[0]:,.2f}**")
