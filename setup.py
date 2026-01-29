from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'pick_and_place'

setup(
    name=package_name,
    version='0.0.0',
    # Change 1: Humne 'find_packages' use kiya hai taake wo sub-folders dhoond le
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Tumhari URDF aur Launch files
        ('share/' + package_name + '/urdf', ['urdf/robot_arm.urdf']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@gmail.com',
    description='Pick and Place Robot Project',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'start_robot = pick_and_place.main_node:main',
        ],
    },
)
