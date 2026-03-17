import streamlit as st
import pandas as pd
import pickle

# Load model and feature list
model = pickle.load(open("crop_yield_model.pkl", "rb"))
features = pickle.load(open("model_features.pkl", "rb"))

st.title("Crop Yield Prediction System")

st.write("Enter the environmental factors to predict crop yield")

# User Inputs
year = st.number_input("Year", min_value=1980, max_value=2030, step=1)
rainfall = st.number_input("Rainfall (mm)")
temperature = st.number_input("Average Temperature")
pesticides = st.number_input("Pesticides (tonnes)")

# Country and Crop selection
countries = [col.replace("Area_", "")
             for col in features if col.startswith("Area_")]
crops = [col.replace("Item_", "")
         for col in features if col.startswith("Item_")]

country = st.selectbox("Select Country", countries)
crop = st.selectbox("Select Crop", crops)

if st.button("Predict Yield"):

    # Create empty row with all model features
    input_data = pd.DataFrame(columns=features)
    input_data.loc[0] = 0

    # Fill numeric features
    input_data["Year"] = year
    input_data["Rainfall"] = rainfall
    input_data["Avg_Temperature"] = temperature
    input_data["Pesticides_tonnes"] = pesticides

    # Activate selected country and crop
    input_data[f"Area_{country}"] = 1
    input_data[f"Item_{crop}"] = 1

    # Predict
    prediction = model.predict(input_data)

    st.success(f"Predicted Crop Yield: {prediction[0]:.2f}")
