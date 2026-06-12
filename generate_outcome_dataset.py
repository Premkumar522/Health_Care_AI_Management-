import pandas as pd
import numpy as np

np.random.seed(42)

records = []

for _ in range(500):

    age = np.random.randint(20, 85)
    bp = np.random.randint(90, 190)
    sugar = np.random.randint(70, 250)
    bmi = round(np.random.uniform(18, 40), 1)

    risk_score = 0

    if age > 60:
        risk_score += 1

    if bp > 150:
        risk_score += 1

    if sugar > 180:
        risk_score += 1

    if bmi > 32:
        risk_score += 1

    outcome = 1 if risk_score >= 2 else 0

    records.append([
        age,
        bp,
        sugar,
        bmi,
        outcome
    ])

df = pd.DataFrame(
    records,
    columns=[
        "Age",
        "BP",
        "Sugar",
        "BMI",
        "Outcome"
    ]
)

df.to_csv(
    "datasets/outcome_data.csv",
    index=False
)

print("500 Outcome Records Generated")