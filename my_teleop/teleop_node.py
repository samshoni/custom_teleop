#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, tty, termios

class TeleopNode(Node):
    def __init__(self):
        super().__init__('custom_teleop')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('✅ Custom Teleop Node Started')
        self.settings = termios.tcgetattr(sys.stdin)
        self.run()

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def run(self):
        msg = Twist()
        try:
            while rclpy.ok():
                key = self.get_key()
                if key == 'w':
                    msg.linear.x = 0.2
                    msg.angular.z = 0.0
                elif key == 's':
                    msg.linear.x = -0.2
                    msg.angular.z = 0.0
                elif key == 'a':
                    msg.linear.x = 0.0
                    msg.angular.z = 0.5
                elif key == 'd':
                    msg.linear.x = 0.0
                    msg.angular.z = -0.5
                elif key == ' ':
                    msg.linear.x = 0.0
                    msg.angular.z = 0.0
                elif key == 'q':
                    break
                else:
                    continue

                self.publisher_.publish(msg)

        except Exception as e:
            self.get_logger().error(str(e))

        finally:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    node.destroy_node()
    rclpy.shutdown()
