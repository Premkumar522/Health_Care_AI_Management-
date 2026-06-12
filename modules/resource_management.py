import streamlit as st
import pandas as pd
import plotly.express as px
from modules import resource_management

def show():

    st.title(
        "🏥 Resource Allocation Module"
    )

    df = pd.read_csv(
        "datasets/hospital_resources.csv"
    )

    st.subheader(
        "Current Resource Data"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.subheader(
        "Resource Demand Analysis"
    )

    fig = px.scatter(
        df,
        x="Ventilators",
        y="DemandScore",
        size="OxygenUnits",
        hover_data=["Equipment"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    avg_demand = round(
        df["DemandScore"].mean(),
        2
    )

    st.metric(
        "Average Demand",
        avg_demand
    )

    if avg_demand > 200:

        st.warning(
            "High Resource Demand Detected"
        )

    else:

        st.success(
            "Resource Levels Stable"
        )