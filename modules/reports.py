import streamlit as st
import pandas as pd
import os
from modules import reports
from database.db import get_connection

from utils.report_generator import (
    generate_patient_csv,
    generate_patient_excel,
    generate_patient_pdf
)


def show():

    st.title("📄 Reporting Module")

    report_type = st.selectbox(
        "Select Report",
        [
            "Patient Report",
            "Doctor Report"
        ]
    )

    conn = get_connection()

    if report_type == "Patient Report":

        df = pd.read_sql_query(
            "SELECT * FROM patients",
            conn
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

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Generate CSV"):

            filename = (
                f"reports/{report_type}.csv"
            )

            generate_patient_csv(
                df,
                filename
            )

            st.success(
                "CSV Generated"
            )

            with open(filename, "rb") as file:

                st.download_button(
                    "Download CSV",
                    file,
                    file_name=os.path.basename(filename)
                )

    with col2:

        if st.button("Generate Excel"):

            filename = (
                f"reports/{report_type}.xlsx"
            )

            generate_patient_excel(
                df,
                filename
            )

            st.success(
                "Excel Generated"
            )

            with open(filename, "rb") as file:

                st.download_button(
                    "Download Excel",
                    file,
                    file_name=os.path.basename(filename)
                )

    with col3:

        if st.button("Generate PDF"):

            filename = (
                f"reports/{report_type}.pdf"
            )

            generate_patient_pdf(
                df,
                filename
            )

            st.success(
                "PDF Generated"
            )

            with open(filename, "rb") as file:

                st.download_button(
                    "Download PDF",
                    file,
                    file_name=os.path.basename(filename)
                )