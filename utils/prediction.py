import joblib
import numpy as np


def load_disease_model():
    return joblib.load("models/disease_model.pkl")


def load_outcome_model():
    return joblib.load("models/outcome_model.pkl")


def predict_disease(age, bp, sugar, cholesterol, bmi):

    model = load_disease_model()

    features = np.array([
        [age, bp, sugar, cholesterol, bmi]
    ])

    prediction = model.predict(features)[0]

    probability = max(
        model.predict_proba(features)[0]
    ) * 100

    return prediction, round(probability, 2)


def predict_outcome(age, bp, sugar, bmi):

    model = load_outcome_model()

    features = np.array([
        [age, bp, sugar, bmi]
    ])

    prediction = model.predict(features)[0]

    probability = max(
        model.predict_proba(features)[0]
    ) * 100

    return prediction, round(probability, 2)