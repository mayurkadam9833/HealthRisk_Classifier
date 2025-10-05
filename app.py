import base64
import streamlit as st 
import pandas as pd
from pathlib import Path
from src.HealthRisk_Classifier.pipeline.prediction_pipeline import Prediction_pipeline

st.title("``Health Risk classifier``")
st.markdown("``This web application allows users to input personal health and lifestyle data to predict health risk categories.``")

# Function to set background image using base64 encoding
def get_background(image_file): 
    with open(image_file,"rb")as file: 
        data=file.read()
        encoded = base64.b64encode(data).decode()

        css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Setting background image
get_background(Path(".streamlit") / "background.png")

# Create columns for side-by-side inputs
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("``Age``", min_value=0, max_value=120)
    Glucose = st.number_input("``Glucose Level``")
    Blood_Pressure = st.number_input("``Blood Pressure``")
    BMI = st.number_input("``BMI``")

with col2:
    Oxygen_Saturation = st.number_input("``Oxygen Saturation``")
    LengthOfStay = st.number_input("``Length of Stay``")
    Cholesterol = st.number_input("``Cholesterol``")
    Triglycerides = st.number_input("``Triglycerides``")

with col3:
    HbA1c = st.number_input("``HbA1c``")
    Diet_Score = st.number_input("``Diet Score``")
    Physical_Activity = st.number_input("``Physical Activity``")
    Stress_Level = st.number_input("``Stress Level``")

# Another row for remaining features
col4, col5 = st.columns(2)
with col4:
    Sleep_Hours = st.number_input("``Sleep Hours``")
    Alcohol = st.selectbox("Alcohol", ["Yes", "No"],key="alcohol")
with col5:
    Family_History = st.selectbox("``Family History``", ["Yes", "No"],key="family_history")
    Smoking = st.selectbox("``Smoking``", ["Yes", "No"],key="smoking")

if st.button("Health Risk"): 
    Smoking = 1 if Smoking == "Yes" else 0
    Alcohol = 1 if Alcohol == "Yes" else 0
    Family_History = 1 if Family_History == "Yes" else 0
    input_data = pd.DataFrame({
    "Age": [age],
    "Glucose": [Glucose],
    "Blood Pressure": [Blood_Pressure],
    "BMI": [BMI],
    "Oxygen Saturation": [Oxygen_Saturation],
    "LengthOfStay": [LengthOfStay],
    "Cholesterol": [Cholesterol],
    "Triglycerides": [Triglycerides],
    "HbA1c": [HbA1c],
    "Smoking": [Smoking],
    "Alcohol": [Alcohol],
    "Physical Activity": [Physical_Activity],
    "Diet Score": [Diet_Score],
    "Family History": [Family_History],
    "Stress Level": [Stress_Level],
    "Sleep Hours": [Sleep_Hours]})
    pipeline=Prediction_pipeline()
    prediction = pipeline.prediction(input_data)
    st.success(f"Predicted Class: {prediction[0]}")

    