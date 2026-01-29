import rclpy
import time
from rclpy.node import Node
from pick_and_place.controller.robot_controller import RobotController
from pick_and_place.visualizer.marker_manager import MarkerManager

class IndustrialSorter(Node):
    def __init__(self):
        super().__init__('industrial_sorter')
        self.controller = RobotController(self)
        self.markers = MarkerManager(self)
        
        # Color Tasks: [Base, Shoulder, Elbow, Wrist]
        self.TASKS = [
            {'name': 'RED',   'rgb': [1.0, 0.0, 0.0], 'pick': [0.5, 0.5, -0.5, 0.0], 'place': [-0.5, 0.5, -0.5, 0.0]},
            {'name': 'GREEN', 'rgb': [0.0, 1.0, 0.0], 'pick': [0.8, 0.4, -0.4, 0.0], 'place': [-0.8, 0.4, -0.4, 0.0]},
            {'name': 'BLUE',  'rgb': [0.0, 0.0, 1.0], 'pick': [1.0, 0.3, -0.3, 0.0], 'place': [-1.0, 0.3, -0.3, 0.0]}
        ]
        self.run_process()

    def run_process(self):
        time.sleep(2) # RViz setup ka wait
        for task in self.TASKS:
            # 1. Spawn Cube
            self.markers.publish_cube(99, task['rgb'], [0.5, 0.0, 0.05])
            self.get_logger().info(f"Moving to pick {task['name']} Cube...")
            time.sleep(2) # Taake nazar aaye
            
            # 2. Pick Move (Very Slow)
            self.controller.move_to(task['pick'])
            time.sleep(4) # 4 second ruke ga yahan
            
            # 3. Place Move
            self.get_logger().info(f"Placing {task['name']} Cube...")
            self.controller.move_to(task['place'])
            time.sleep(4)
            
            # 4. Finish
            self.markers.publish_cube(99, task['rgb'], [-0.5, 0.0, 0.05])
            time.sleep(2)

def main():
    rclpy.init()
    node = IndustrialSorter()
    rclpy.shutdown()
