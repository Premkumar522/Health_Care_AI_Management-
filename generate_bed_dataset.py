import pandas as pd
import numpy as np

np.random.seed(42)

records = []

for day in range(1, 501):

    admissions = np.random.randint(20, 100)
    occupied = np.random.randint(50, 250)
    available = 300 - occupied

    future_requirement = int(
        occupied + admissions * 0.5
    )

    records.append([
        day,
        admissions,
        occupied,
        available,
        future_requirement
    ])

df = pd.DataFrame(
    records,
    columns=[
        "Day",
        "Admissions",
        "OccupiedBeds",
        "AvailableBeds",
        "FutureBedsRequired"
    ]
)

df.to_csv(
    "datasets/bed_data.csv",
    index=False
)

print("Bed Dataset Generated")