import pandas as pd  # CSV dosyasını okumak için pandas kütüphanesini kullanıyoruz
import matplotlib.pyplot as plt  # Grafik çizmek için matplotlib kullanıyoruz
import seaborn as sns  # Grafiklerin görünümünü güzelleştirmek için seaborn kullanıyoruz

sns.set_theme(style="darkgrid")

df = pd.read_csv("flight_data.csv")

time = df["Time"]
altitude = df["Altitude"]
speed = df["Speed"]
distance = df["Distance"]

plt.figure(figsize=(10, 6))

plt.plot(time, altitude, label='Altitude (m)', marker='o')  # Yükseklik için noktalar
plt.plot(time, speed, label='Speed (m/s)', marker='s')      # Hız için kare işaretler
plt.plot(time, distance, label='Distance (m)', marker='^')  # Mesafe için üçgen işaretler

plt.title('Mini Drone Flight Data')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()
