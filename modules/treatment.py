import streamlit as st
from utils.recommendation import get_treatment
from modules import treatment

def show():

    st.title(
        "💊 Treatment Recommendation"
    )

    disease = st.selectbox(
        "Select Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease"
        ]
    )

    if st.button(
        "Generate Recommendation"
    ):

        result = get_treatment(
            disease
        )

        st.subheader(
            "Recommended Specialist"
        )

        st.write(
            result["specialist"]
        )

        st.subheader(
            "Recommended Tests"
        )

        for test in result["tests"]:
            st.write("✔", test)

        st.subheader(
            "Treatment Plan"
        )

        st.info(
            result["treatment"]
        )