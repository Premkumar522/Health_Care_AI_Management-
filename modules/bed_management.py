import streamlit as st
from utils.forecasting import predict_bed_requirement
from modules import bed_management

def show():

    st.title(
        "🛏️ Bed Management System"
    )

    total_beds = st.number_input(
        "Total Beds",
        value=300
    )

    occupied = st.number_input(
        "Occupied Beds",
        value=150
    )

    admissions = st.number_input(
        "Today's Admissions",
        value=50
    )

    available = total_beds - occupied

    st.metric(
        "Available Beds",
        available
    )

    if st.button(
        "Predict Future Requirement"
    ):

        prediction = predict_bed_requirement(
            admissions,
            occupied,
            available
        )

        st.success(
            f"Expected Bed Requirement : {prediction}"
        )

        shortage = prediction - total_beds

        if shortage > 0:

            st.error(
                f"Shortage Risk : {shortage} Beds"
            )

        else:

            st.success(
                "Current Capacity Sufficient"
            )