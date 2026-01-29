Industrial RGB Pick & Place Robot
================================

A professional 4-Axis Industrial Robot Arm simulation built with
ROS2 Foxy for Jetson Nano.


FEATURES
--------

- Industrial Design:
  Realistic 4-axis orange industrial arm URDF model.

- Autonomous Sorting:
  Intelligent logic to sort Red, Green, and Blue cubes.

- RViz Integration:
  Real-time visualization using JointStates and Marker Arrays.

- Smooth Motion:
  Optimized timing (4 seconds per move) for clear process demonstration.


PROJECT STRUCTURE
-----------------

pick_and_place/
|
|-- urdf/
|   Contains the 3D robot model description
|
|-- launch/
|   Launch files to start the simulation environment
|
|-- pick_and_place/
|   Core Python logic, controllers, and planners
|
|-- README.txt


HOW TO RUN
----------

1) Build the Project

Open terminal and run:

cd ~/ros2_ws
colcon build --packages-select pick_and_place
source install/setup.bash


2) Launch Simulation (Terminal 1)

ros2 launch pick_and_place display.launch.py

RViz Settings:
- Fixed Frame: base_link
- Add Marker
- Topic: /visualization_marker


3) Start Robot Logic (Terminal 2)

ros2 run pick_and_place start_robot


REQUIREMENTS
------------

- ROS2 Foxy
- Python 3
- RViz2


FINAL CHECKLIST
---------------

1) File Name:
   README.txt

2) Location:
   ~/Documents/ros2_ws/src/pick_and_place/

3) Upload:
   Upload this file along with the complete src folder to GitHub

