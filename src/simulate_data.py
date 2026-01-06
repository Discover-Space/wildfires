import random
import pandas as pd

rows = []

for _ in range(500):
    temp = random.uniform(20, 45)
    humidity = random.uniform(10, 70)
    wind = random.uniform(0, 30)
    smoke = random.randint(50, 500)

    fire = 1 if temp > 35 and humidity < 30 and smoke > 300 else 0
    rows.append([temp, humidity, wind, smoke, fire])

df = pd.DataFrame(
    rows,
    columns=["temperature", "humidity", "wind", "smoke", "fire"]
)

df.to_csv("data/wildfire_data.csv", index=False)
print("Simulated data saved!")

