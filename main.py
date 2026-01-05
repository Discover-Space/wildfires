from predict import predict_risk

sample_data = [
    (38, 22, 18, 410),
    (32, 45, 10, 180),
    (27, 55, 5, 90)
]

for t, h, w, s in sample_data:
    risk = predict_risk(t, h, w, s)
    print(f"T={t}°C H={h}% W={w} S={s} → {risk}")



