import streamlit as st 
import pandas as pd
from src.HealthRisk_Classifier.pipeline.prediction_pipeline import Prediction_pipeline

st.title("Health Risk classifier")


age = st.sidebar.number_input(label="Age", min_value=10, max_value=90)
Glucose = st.sidebar.number_input(label="Glucose", min_value=20, max_value=500)
Blood_Pressure = st.sidebar.number_input(label="Blood Pressure", min_value=20, max_value=500)
BMI = st.sidebar.number_input(label="BMI", min_value=10, max_value=100)
Oxygen_Saturation = st.sidebar.number_input(label="Oxygen Saturation", min_value=20, max_value=100)
LengthOfStay = st.sidebar.number_input(label="Length of Stay (Days)", min_value=1, max_value=365)
Cholesterol = st.sidebar.number_input(label="Cholesterol", min_value=50, max_value=400)
Triglycerides = st.sidebar.number_input(label="Triglycerides", min_value=50, max_value=500)
HbA1c = st.sidebar.number_input(label="HbA1c", min_value=3.0, max_value=15.0)
Physical_Activity = st.sidebar.number_input(label="Physical Activity (hours/week)", min_value=0, max_value=50)
Diet_Score = st.sidebar.number_input(label="Diet Score", min_value=0, max_value=100)
Stress_Level = st.sidebar.number_input(label="Stress Level (1–10)", min_value=1, max_value=10)
Sleep_Hours = st.sidebar.number_input(label="Sleep Hours", min_value=1, max_value=24)

# Categorical inputs
Smoking = st.sidebar.selectbox("Smoking", ["Yes", "No"])
Alcohol = st.sidebar.selectbox("Alcohol", ["Yes", "No"])
Family_History = st.sidebar.selectbox("Family History", ["Yes", "No"])


if st.button("health risk"): 
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

    