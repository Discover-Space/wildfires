import serial
import time
from predict import predict_fire

# ===== Configure Arduino serial =====
arduino_port = "COM3"  # <-- change to your Arduino port
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # wait for Arduino to reset

print("Reading live values from Arduino dials...")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if not line:
            continue

        # Arduino prints: "Dial 1: 512 | Dial 2: 300 | Dial 3: 1023 | Dial 4: 100"
        parts = line.split('|')
        values = [int(p.split(':')[1]) for p in parts]

        dial1, dial2, dial3, dial4 = values

        # Map dial values to wildfire parameters
        temperature = 20 + (dial1 / 1023) * 25   # 20–45°C
        humidity = 10 + (dial2 / 1023) * 60      # 10–70%
        wind = (dial3 / 1023) * 30               # 0–30
        smoke = 50 + int((dial4 / 1023) * 450)   # 50–500

        # Predict fire risk
        risk = predict_fire(temperature, humidity, wind, smoke)

        # Print nicely
        print(
            f"T={temperature:.1f}°C | H={humidity:.1f}% | "
            f"W={wind:.1f} | S={smoke} → {risk}"
        )

        time.sleep(0.1)  # small delay to avoid flooding

    except KeyboardInterrupt:
        print("Stopping...")
        break
    except Exception as e:
        print("Error:", e)
