import streamlit as st

from database.db import create_tables

# Import Pages
from modules import (
    login,
    dashboard,
    patient,
    doctor,
    appointments,
    disease_prediction,
    treatment,
    outcome_prediction,
    bed_management,
    resource_management,
    chatbot,
    reports
)
# Create Database Tables
create_tables()

# Streamlit Config
st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# LOGIN CHECK
# -----------------------------

if st.session_state.logged_in:

    st.sidebar.title("🏥 Healthcare AI System")

    st.sidebar.success(
        f"Logged in as: {st.session_state.user}"
    )

    page = st.sidebar.selectbox(
        "Select Module",
        [
            "Dashboard",
            "Patient Management",
            "Doctor Management",
            "Appointment Management",
            "Disease Prediction",
            "Treatment Recommendation",
            "Outcome Prediction",
            "Bed Management",
            "Resource Management",
            "AI Chatbot",
            "Reports"
        ]
    )

    # Logout
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # -----------------------------
    # PAGE ROUTING
    # -----------------------------

    if page == "Dashboard":
        dashboard.show()

    elif page == "Patient Management":
        patient.show()

    elif page == "Doctor Management":
        doctor.show()

    elif page == "Appointment Management":
        appointments.show()

    elif page == "Disease Prediction":
        disease_prediction.show()

    elif page == "Treatment Recommendation":
        treatment.show()

    elif page == "Outcome Prediction":
        outcome_prediction.show()

    elif page == "Bed Management":
        bed_management.show()

    elif page == "Resource Management":
        resource_management.show()

    elif page == "AI Chatbot":
        chatbot.show()

    elif page == "Reports":
        reports.show()

else:
    login.show()