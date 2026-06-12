import streamlit as st
import pandas as pd
from database.db import get_connection
from modules import patient

def show():

    st.title("🧑 Patient Management")

    menu = [
        "Add Patient",
        "View Patients"
    ]

    choice = st.sidebar.radio(
        "Patient Menu",
        menu
    )

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "Add Patient":

        name = st.text_input("Name")
        age = st.number_input("Age", 1, 120)

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        weight = st.number_input(
            "Weight"
        )

        height = st.number_input(
            "Height"
        )

        blood = st.selectbox(
            "Blood Group",
            ["A+","A-","B+","B-",
             "AB+","AB-","O+","O-"]
        )

        history = st.text_area(
            "Medical History"
        )

        allergies = st.text_area(
            "Allergies"
        )

        insurance = st.text_input(
            "Insurance"
        )

        if st.button("Save Patient"):

            cursor.execute("""
            INSERT INTO patients(
            name,
            age,
            gender,
            weight,
            height,
            blood_group,
            medical_history,
            allergies,
            insurance
            )
            VALUES(?,?,?,?,?,?,?,?,?)
            """,

            (
                name,
                age,
                gender,
                weight,
                height,
                blood,
                history,
                allergies,
                insurance
            ))

            conn.commit()

            st.success(
                "Patient Added Successfully"
            )

    else:

        df = pd.read_sql_query(
            "SELECT * FROM patients",
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    conn.close()