import pandas as pd
import numpy as np

np.random.seed(42)

records = []

for _ in range(500):

    age = np.random.randint(20, 85)
    bp = np.random.randint(90, 190)
    sugar = np.random.randint(70, 250)
    cholesterol = np.random.randint(120, 320)
    bmi = round(np.random.uniform(18, 40), 1)

    if sugar > 160 and bmi > 28:
        disease = "Diabetes"

    elif bp > 150 and cholesterol > 240:
        disease = "Heart Disease"

    elif bp > 140 and sugar > 140:
        disease = "Kidney Disease"

    else:
        disease = "Healthy"

    records.append([
        age,
        bp,
        sugar,
        cholesterol,
        bmi,
        disease
    ])

df = pd.DataFrame(
    records,
    columns=[
        "Age",
        "BP",
        "Sugar",
        "Cholesterol",
        "BMI",
        "Disease"
    ]
)

df.to_csv(
    "datasets/disease_data.csv",
    index=False
)

print("500 Disease Records Generated")
