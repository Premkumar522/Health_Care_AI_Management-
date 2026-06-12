def get_treatment(disease):

    recommendations = {

        "Diabetes": {
            "specialist": "Endocrinologist",
            "tests": [
                "HbA1c",
                "Blood Sugar Test"
            ],
            "treatment":
            "Lifestyle changes, insulin therapy if required."
        },

        "Heart Disease": {
            "specialist": "Cardiologist",
            "tests": [
                "ECG",
                "2D Echo",
                "Lipid Profile"
            ],
            "treatment":
            "Cardiac monitoring and medication."
        },

        "Kidney Disease": {
            "specialist": "Nephrologist",
            "tests": [
                "Creatinine Test",
                "Urine Analysis"
            ],
            "treatment":
            "Kidney function monitoring."
        }

    }

    return recommendations.get(
        disease,
        {
            "specialist": "General Physician",
            "tests": ["Basic Health Checkup"],
            "treatment": "Consult doctor."
        }
    )