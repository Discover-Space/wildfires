from predict import predict_fire

samples = [
    (38, 22, 18, 410),
    (28, 55, 8, 120)
]

for s in samples:
    print(s, predict_fire(*s))
