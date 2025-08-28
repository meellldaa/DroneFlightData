import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation

print("Welcome to DroneFlightData Visualizer!")
print("How would you like to enter the data?")
print("1 - Enter data manually")
print("2 - Load data from CSV file")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    count = int(input("How many time points will you enter? "))
    time = get_data("Time (seconds)", count)
    altitude = get_data("Altitude (meters)", count)
    speed = get_data("Speed (m/s)", count)
    distance = get_data("Distance (meters)", count)

elif choice == "2":
    try:
        df = pd.read_csv("flight_data.csv")
        time = df["Time"]
        altitude = df["Altitude"]
        speed = df["Speed"]
        distance = df["Distance"]
    except FileNotFoundError:
        print("CSV file not found. Please make sure 'flight_data.csv' exists.")
        exit()

else:
    print("Invalid choice. Please run the program again.")
    exit()


def get_data(label, count):
    print(f"Enter {label} values ({count} values expected):")
    data = []
    for i in range(count):
        while True:
            try:
                value = float(input(f"{label} #{i+1}: "))
                data.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return data


plt.figure(figsize=(10, 6))
plt.plot(time, altitude, label='Altitude (m)', marker='o')
plt.plot(time, speed, label='Speed (m/s)', marker='s')
plt.plot(time, distance, label='Distance (m)', marker='^')

plt.title('Mini Drone Flight Data')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
