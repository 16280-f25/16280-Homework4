#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
import math
import csv

class ImuOdomSubscriber(Node):
    def __init__(self):
        super().__init__('imu_odom_subscriber')
        #TODO:
        # Define QoS profile
        qos_profile = ...


        #TODO:
        # Initialize subscribers for /imu and /odom topics
        self.imu_sub = ...
        self.odom_sub = ...



        # Initialize the kinematic model and complementary filter variables
        self.last_time = None
        self.position = [0.0, 0.0, 0.0]  # [x, y, theta]
        self.orientation = [0.0, 0.0, 0.0]  # [roll, pitch, yaw]
        self.fused_var = [0.0, 0.0, 0.0]  # [x, y, yaw]
        self.linear_velocity = 0.0
        self.angular_velocity = 0.0

        # Data storage
        self.time_stamps = []
        self.odom_data = []
        self.orientation_data = []
        self.fused_data = []

    def imu_callback(self, imu_msg):
        # IMU orientation data

        #TODO:
        # read orientation and store it in q
        q = ...

        # get euler angle from quaternion q
        euler = ...

        self.orientation = euler  # [roll, pitch, yaw]


    def odom_callback(self, odom_msg):
        # Odometry data (position and velocity)
        current_time = self.get_clock().now().to_msg()

        if self.last_time:
            # Compute delta time
            dt = (current_time.sec - self.last_time.sec) + (current_time.nanosec - self.last_time.nanosec) / 1e9
        else:
            dt = 0.0  # First message, no delta time

        #TODO:
        # Extract position and x_velocity from Odometry
        x =...
        y = ...
        linear_velocity = ...

        # pass quaterion from odom message
        theta = self.get_yaw_from_quaternion(...)
        

        self.position = [x,y,theta]

        #TODO:
        # Apply the complementary filter: Combine IMU orientation and Odometry position
        alpha = ...  # filter constant, should be between 0 and 1
        self.fused_var[2] = ... # fused yaw from IMU and Odometry



        # Use fused orientation (yaw) to update position using the kinematic model
        if dt > 0:

            #TODO:
            # Update position using the fused yaw (orientation) , use the equations from kinematic model
            
            self.position[0] += ... # Use fused yaw
            self.position[1] += ... # Use fused yaw
            self.position[2] = ...  # Set the fused yaw as the current orientation

        # Store data for CSV
        self.time_stamps.append(current_time.sec + current_time.nanosec / 1e9)
        self.odom_data.append((x, y))  # Store x and y position

        self.fused_data.append((self.position[0], self.position[1], self.position[2]))  # Store fused x, y, and fused yaw

        self.last_time = current_time

    def quaternion_to_euler(self, q):
        """Convert quaternion to Euler angles."""
        x, y, z, w = q.x, q.y, q.z, q.w
        roll = math.atan2(2.0 * (w * x + y * z), 1.0 - 2.0 * (x * x + y * y))
        pitch = math.asin(2.0 * (w * y - z * x))
        yaw = math.atan2(2.0 * (w * z + x * y), 1.0 - 2.0 * (y * y + z * z))
        return [roll, pitch, yaw]

    def get_yaw_from_quaternion(self, quat):
        """Get yaw (rotation around Z-axis) from a quaternion."""
        siny_cosp = 2.0 * (quat.w * quat.z + quat.x * quat.y)
        cosy_cosp = 1.0 - 2.0 * (quat.y * quat.y + quat.z * quat.z)
        return math.atan2(siny_cosp, cosy_cosp)

    def save_data(self):
        """Save data to CSV file."""
        with open('fused_data.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'Odometry X', 'Odometry Y', 'Fused X', 'Fused Y', 'Fused Yaw'])
            for i in range(len(self.time_stamps)):
                writer.writerow([self.time_stamps[i], self.odom_data[i][0], self.odom_data[i][1], self.fused_data[i][0], self.fused_data[i][1], self.fused_data[i][2]])

def main(args=None):
    rclpy.init(args=args)
    node = ImuOdomSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Save the data to a CSV file before shutting down
        node.save_data()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
