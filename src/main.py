import pandas as pd
from predict import predict_fire

# Read CSV data
df = pd.read_csv("data/simulated_wildfire_data.csv")
df = pd.read_csv("data/wildfire_data.csv")

# Use only the input columns (ignore the label)
for i, row in df.head(10).iterrows():  # first 10 rows
    temp = row["temperature"]
    humidity = row["humidity"]
    wind = row["wind"]
    smoke = row["smoke"]

    risk = predict_fire(temp, humidity, wind, smoke)

    print(
        f"T={temp:.1f}°C | H={humidity:.1f}% | "
        f"W={wind:.1f} | S={smoke} → {risk}"
    )
