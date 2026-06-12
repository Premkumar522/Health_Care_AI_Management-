import streamlit as st
import pandas as pd
import plotly.express as px
from modules import dashboard

def show():

    st.title(
        "📊 Healthcare Analytics Dashboard"
    )

    try:

        patient_df = pd.read_sql_query(
            "SELECT * FROM patients",
            __import__(
                "database.db",
                fromlist=["get_connection"]
            ).get_connection()
        )

        doctor_df = pd.read_sql_query(
            "SELECT * FROM doctors",
            __import__(
                "database.db",
                fromlist=["get_connection"]
            ).get_connection()
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Patients",
                len(patient_df)
            )

        with col2:
            st.metric(
                "Total Doctors",
                len(doctor_df)
            )

        with col3:
            st.metric(
                "System Status",
                "Active"
            )

        st.divider()

        st.subheader(
            "Patient Age Distribution"
        )

        if len(patient_df) > 0:

            fig = px.histogram(
                patient_df,
                x="age",
                nbins=10,
                title="Patient Age Analysis"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.subheader(
            "Gender Distribution"
        )

        if len(patient_df) > 0:

            gender_chart = px.pie(
                patient_df,
                names="gender",
                title="Gender Distribution"
            )

            st.plotly_chart(
                gender_chart,
                use_container_width=True
            )

    except Exception as e:

        st.error(
            f"Dashboard Error: {e}"
        )