import streamlit as st
import pandas as pd
from database.db import get_connection
from modules import patient

def show():

    st.title("📅 Appointment Management")

    menu = [
        "Book Appointment",
        "View Appointments",
        "Cancel Appointment"
    ]

    choice = st.sidebar.radio(
        "Appointment Menu",
        menu
    )

    conn = get_connection()
    cursor = conn.cursor()

    # --------------------------
    # BOOK APPOINTMENT
    # --------------------------

    if choice == "Book Appointment":

        st.subheader("Book New Appointment")

        patient_df = pd.read_sql_query(
            "SELECT name FROM patients",
            conn
        )

        doctor_df = pd.read_sql_query(
            "SELECT name FROM doctors",
            conn
        )

        if len(patient_df) == 0:
            st.warning(
                "Please add patients first."
            )
            return

        if len(doctor_df) == 0:
            st.warning(
                "Please add doctors first."
            )
            return

        patient_name = st.selectbox(
            "Select Patient",
            patient_df["name"]
        )

        doctor_name = st.selectbox(
            "Select Doctor",
            doctor_df["name"]
        )

        appointment_date = st.date_input(
            "Appointment Date"
        )

        appointment_time = st.time_input(
            "Appointment Time"
        )

        if st.button("Book Appointment"):

            cursor.execute(
                """
                INSERT INTO appointments
                (
                patient_name,
                doctor_name,
                appointment_date,
                appointment_time,
                status
                )
                VALUES (?,?,?,?,?)
                """,
                (
                    patient_name,
                    doctor_name,
                    str(appointment_date),
                    str(appointment_time),
                    "Scheduled"
                )
            )

            conn.commit()

            st.success(
                "Appointment Booked Successfully"
            )

    # --------------------------
    # VIEW APPOINTMENTS
    # --------------------------

    elif choice == "View Appointments":

        st.subheader("Appointment List")

        df = pd.read_sql_query(
            """
            SELECT * FROM appointments
            """,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # --------------------------
    # CANCEL APPOINTMENT
    # --------------------------

    elif choice == "Cancel Appointment":

        st.subheader(
            "Cancel Appointment"
        )

        df = pd.read_sql_query(
            """
            SELECT * FROM appointments
            """,
            conn
        )

        if len(df) == 0:

            st.warning(
                "No Appointments Found"
            )

        else:

            appointment_id = st.selectbox(
                "Select Appointment ID",
                df["id"]
            )

            if st.button(
                "Cancel Appointment"
            ):

                cursor.execute(
                    """
                    UPDATE appointments
                    SET status='Cancelled'
                    WHERE id=?
                    """,
                    (
                        int(appointment_id),
                    )
                )

                conn.commit()

                st.success(
                    "Appointment Cancelled"
                )

    conn.close()