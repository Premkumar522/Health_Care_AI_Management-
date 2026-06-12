import streamlit as st
from utils.prediction import predict_disease
from modules import disease_prediction

def show():

    st.title("🩺 AI Disease Prediction")

    age = st.number_input(
        "Age",
        1,
        120
    )

    bp = st.number_input(
        "Blood Pressure"
    )

    sugar = st.number_input(
        "Sugar Level"
    )

    cholesterol = st.number_input(
        "Cholesterol"
    )

    bmi = st.number_input(
        "BMI"
    )

    if st.button("Predict Disease"):

        disease, score = predict_disease(
            age,
            bp,
            sugar,
            cholesterol,
            bmi
        )

        st.success(
            f"Predicted Disease : {disease}"
        )

        st.info(
            f"Risk Score : {score}%"
        )

        if score > 80:
            st.error("High Risk")

        elif score > 50:
            st.warning("Moderate Risk")

        else:
            st.success("Low Risk")