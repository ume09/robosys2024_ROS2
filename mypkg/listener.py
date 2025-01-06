import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
  pub = node.create_subscription(Int16, "time_info", cb, 10)
  rclpy.spin(node)
_info
