import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "fire_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_fire(temp, humidity, wind, smoke):
    # Create DataFrame with column names
    df = pd.DataFrame([[temp, humidity, wind, smoke]],
                      columns=["temperature", "humidity", "wind", "smoke"])
    
    prediction = model.predict(df)[0]
    
    # Optional: add probability output
    prob = model.predict_proba(df)[0][1]  # probability of fire
    return f"🔥 Fire Risk ({prob*100:.1f}%)" if prediction == 1 else f"✅ No Fire Risk ({(100-prob*100):.1f}%)"
