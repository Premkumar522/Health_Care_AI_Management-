import joblib
import numpy as np


def load_bed_model():

    return joblib.load(
        "models/bed_forecast.pkl"
    )


def predict_bed_requirement(
    admissions,
    occupied,
    available
):

    model = load_bed_model()

    data = np.array([
        [
            admissions,
            occupied,
            available
        ]
    ])

    prediction = model.predict(data)[0]

    return round(prediction)