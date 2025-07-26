#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from rclpy.qos import QoSProfile
from message_filters import Subscriber, ApproximateTimeSynchronizer


class ImuOdomSubscriber(Node):
    def __init__(self):
        super().__init__('imu_odom_subscriber')
        #TODO:
        # Define QoS profile
        qos_profile_imu = ...
        qos_profile_odom = ...
        

        # Initialize subscribers for /imu and /odom topics with QoS profile passed correctly
        self.imu_sub = ...
        self.odom_sub = ...

        #TODO:
        # use Approximate time synchronizer to synchronize the two topics and regeister the callback
        self.ts = ...
        self.ts.registerCallback(self.callback)

    def callback(self, imu_msg, odom_msg):
        # Process synchronized messages here (hint: look at imu_msg and odom_msg attributes)
        self.get_logger().info(...)
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
