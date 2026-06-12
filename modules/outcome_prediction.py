import streamlit as st
from utils.prediction import predict_outcome
from modules import outcome_prediction

def show():

    st.title(
        "🏥 Patient Outcome Prediction"
    )

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

    bmi = st.number_input(
        "BMI"
    )

    if st.button(
        "Predict Outcome"
    ):

        outcome, probability = predict_outcome(
            age,
            bp,
            sugar,
            bmi
        )

        st.success(
            f"Outcome : {outcome}"
        )

        st.info(
            f"Confidence : {probability}%"
        )

        if outcome == 1:
            st.warning(
                "Possible Hospitalization"
            )

        else:
            st.success(
                "Normal Recovery Expected"
            )