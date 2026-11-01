#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") # MODIFY NAME
        self.robot_name_ = "R2D2"
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer = self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot News Station Node has been started!")

    def publish_news(self):
        msg = String()
        msg.data = "Hello this is from "+self.robot_name_ +" the Robot News Station! " 
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
