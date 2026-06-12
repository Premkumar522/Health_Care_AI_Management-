import pandas as pd
import numpy as np

np.random.seed(42)

records = []

for _ in range(500):

    ventilators = np.random.randint(10, 80)
    oxygen = np.random.randint(100, 1000)
    equipment = np.random.randint(20, 200)

    demand = int(
        ventilators * 0.5 +
        oxygen * 0.2 +
        equipment * 0.3
    )

    records.append([
        ventilators,
        oxygen,
        equipment,
        demand
    ])

df = pd.DataFrame(
    records,
    columns=[
        "Ventilators",
        "OxygenUnits",
        "Equipment",
        "DemandScore"
    ]
)

df.to_csv(
    "datasets/hospital_resources.csv",
    index=False
)

print("Resource Dataset Generated Successfully")