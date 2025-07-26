import matplotlib.pyplot as plt
import csv

def load_data(filename='fused_data.csv'):
    time_stamps = []
    
    odom_data = []
    fused_data = []
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            time_stamps.append(float(row[0]))
 
            odom_data.append((float(row[1]), float(row[2])))  # Odometry X, Odometry Y
            fused_data.append((float(row[3]), float(row[4]), float(row[5])))  # Fused X, Fused Y, Fused Yaw

    return time_stamps, odom_data, fused_data


def plot_data(time_stamps, odom_data, fused_data):
    # Extract the x and y values from the data
    odom_x, odom_y = zip(*odom_data)
    fused_x, fused_y, fused_yaw = zip(*fused_data)

    # Create subplots: 5 rows, 1 column
    fig, axs = plt.subplots(5, 1, figsize=(10, 15))

    # Plot Odometry X vs Time
    axs[0].plot(time_stamps, odom_x, label="Odometry X", linestyle='-', marker='x', color='red', markersize=1)
    axs[0].set_title("Odometry X Position Over Time")
    axs[0].set_xlabel("Time (s)")
    axs[0].set_ylabel("X Position (m)")
    axs[0].grid(True)
    axs[0].legend(loc="upper left")

    # Plot Odometry Y vs Time
    axs[1].plot(time_stamps, odom_y, label="Odometry Y", linestyle='-', marker='x', color='red', markersize=1)
    axs[1].set_title("Odometry Y Position Over Time")
    axs[1].set_xlabel("Time (s)")
    axs[1].set_ylabel("Y Position (m)")
    axs[1].grid(True)
    axs[1].legend(loc="upper left")

    # Plot Fused X vs Time
    axs[2].plot(time_stamps, fused_x, label="Fused X", linestyle='-', marker='s', color='green', markersize=1)
    axs[2].set_title("Fused X Position Over Time")
    axs[2].set_xlabel("Time (s)")
    axs[2].set_ylabel("X Position (m)")
    axs[2].grid(True)
    axs[2].legend(loc="upper left")

    # Plot Fused Y vs Time
    axs[3].plot(time_stamps, fused_y, label="Fused Y", linestyle='-', marker='s', color='green', markersize=1)
    axs[3].set_title("Fused Y Position Over Time")
    axs[3].set_xlabel("Time (s)")
    axs[3].set_ylabel("Y Position (m)")
    axs[3].grid(True)
    axs[3].legend(loc="upper left")

    # Plot Fused Yaw (Orientation)
    axs[4].plot(time_stamps, fused_yaw, label="Fused Yaw", linestyle='-', marker='o', color='blue', markersize=1)
    axs[4].set_title("Fused Yaw (Orientation) Over Time")
    axs[4].set_xlabel("Time (s)")
    axs[4].set_ylabel("Yaw (radians)")
    axs[4].grid(True)
    axs[4].legend(loc="upper left")

    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Show the plots
    plt.show()


if __name__ == "__main__":
    time_stamps, odom_data, fused_data = load_data('fused_data.csv')
    plot_data(time_stamps, odom_data, fused_data)
