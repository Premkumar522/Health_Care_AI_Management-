import streamlit as st
import pandas as pd
from database.db import get_connection
from modules import doctor

def show():

    st.title("👨‍⚕️ Doctor Management")

    menu = [
        "Add Doctor",
        "View Doctors"
    ]

    choice = st.sidebar.radio(
        "Doctor Menu",
        menu
    )

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "Add Doctor":

        name = st.text_input(
            "Doctor Name"
        )

        specialization = st.text_input(
            "Specialization"
        )

        qualification = st.text_input(
            "Qualification"
        )

        experience = st.number_input(
            "Experience (Years)",
            0,
            50
        )

        availability = st.text_input(
            "Availability"
        )

        if st.button("Save Doctor"):

            cursor.execute("""
            INSERT INTO doctors(
            name,
            specialization,
            qualification,
            experience,
            availability
            )
            VALUES(?,?,?,?,?)
            """,

            (
                name,
                specialization,
                qualification,
                experience,
                availability
            ))

            conn.commit()

            st.success(
                "Doctor Added Successfully"
            )

    else:

        df = pd.read_sql_query(
            "SELECT * FROM doctors",
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    conn.close()