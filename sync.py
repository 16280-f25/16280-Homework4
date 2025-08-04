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
        #TODO: Define QoS profiles 

        # Initialize subscribers for /imu and /odom topics with QoS profile passed correctly

        #TODO:
        # use Approximate time synchronizer to synchronize the two topics and regeister the callback
        self.ts = ...
        self.ts.registerCallback(self.callback)

    def callback(self, ..., ...):
        pass


def main(args=None):
    rclpy.init(args=args)
    
    # Make a subscriber node, and spin it to run the program


if __name__ == '__main__':
    main()
