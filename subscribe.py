#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from message_filters import Subscriber, ApproximateTimeSynchronizer
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

class ImuOdomSubscriber(Node):
    def __init__(self):
        super().__init__('imu_odom_subscriber')
        #TODO:
        # Define QoS profile
        qos_profile_imu = ...
        qos_profile_odom = ...
        #TODO:
        # Initialize subscribers for /imu and /odom topics with QoS profile passed correctly
        self.imu_sub = ...
        self.odom_sub = ...

    # Log imu and odometry data
    def imu_callback(self, imu_msg):
        # Process messages here
        self.get_logger().info(...)
    def odom_callback(self,odom_msg):
        # Process messages here
        self.get_logger().info(...)


def main(args=None):
    rclpy.init(args=args)
    node = ImuOdomSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
