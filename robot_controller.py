from sensor_msgs.msg import JointState
import rclpy

class RobotController:
    def __init__(self, node):
        self.node = node
        self.publisher = node.create_publisher(JointState, 'joint_states', 10)
        self.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4']

    def move_to(self, positions):
        msg = JointState()
        msg.header.stamp = self.node.get_clock().now().to_msg()
        msg.name = self.joint_names
        msg.position = [float(p) for p in positions]
        self.publisher.publish(msg)
