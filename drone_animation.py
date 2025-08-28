import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = pd.read_csv("flight_data.csv")

time = data["Time"]
altitude = data["Altitude"]

fig, ax = plt.subplots()
ax.set_xlim(min(time), max(time))
ax.set_ylim(min(altitude)-5, max(altitude)+5)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Altitude (m)")
ax.set_title("Drone Altitude Animation")

line, = ax.plot([], [], 'ro-')
def update(i):
    x = time[:i]
    y = altitude[:i]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=len(time)+1, interval=300)
plt.show()
