
def predict_risk(temp, humidity, wind, smoke):
    if temp > 35 and humidity < 30 and smoke > 300:
        return "🔥 HIGH RISK"
    elif temp > 30 and humidity < 40:
        return "⚠️ MEDIUM RISK"
    else:
        return "✅ LOW RISK"

