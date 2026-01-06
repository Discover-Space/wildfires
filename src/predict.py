import joblib

model = joblib.load("models/fire_model.pkl")

def predict_fire(temp, humidity, wind, smoke):
    prediction = model.predict([[temp, humidity, wind, smoke]])[0]
    return "🔥 HIGH RISK" if prediction == 1 else "✅ LOW RISK"
