#!/bin/python3
# If you don't even know where to start, see: https://ros2-tutorial.readthedocs.io
# Author: Murilo M. Marinho, email: murilomarinho@ieee.org
import time
from dqrobotics import *
from sas_robot_kinematics import RobotKinematicsClient
from sas_common import rclcpp_init, rclcpp_Node, rclcpp_spin_some, rclcpp_shutdown


def main(args=None):
    a = DQ([1])
    """
    In this example, everything fits nicely into the main function. The four robot arms in AISP are controllable
    through their respective RobotKinematicsClient. After obtaining their initial task-space values, we command
    each arm to move a bit.
    The `sas_robot_kinematics_constrained_multiarm` node will take care of the inverse kinematics of the whole system,
    while preventing collisions among robots and workspace.

    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclcpp_init()  # Init rclcpp to use the sas python bindings. They do not use rclpy.
        # However, you can also have rclpy nodes active as long as you manage their spin
        # correctly.
        rclcpp_node = rclcpp_Node("aisp_ros2_kinematics_control_example_rclcpp")

        arm_interface_list = [RobotKinematicsClient(rclcpp_node, '/arm1_kinematics'),
                              RobotKinematicsClient(rclcpp_node, '/arm2_kinematics'),
                              RobotKinematicsClient(rclcpp_node, '/arm3_kinematics'),
                              RobotKinematicsClient(rclcpp_node, '/arm4_kinematics')]

        # Wait for all interfaces to be enabled
        all_interfaces_enabled = False
        while not all_interfaces_enabled:
            rclcpp_spin_some(rclcpp_node)  # Spin rclcpp
            all_interfaces_enabled = True
            for arm_interface in arm_interface_list:
                if not arm_interface.is_enabled():
                    all_interfaces_enabled = False
                    break
            time.sleep(0.001)

        # Read initial values of each interface
        arm_counter = 1
        for arm_interface in arm_interface_list:
            print("****************************")
            print("***Initial info for arm {}***".format(arm_counter))
            print("****************************")
            print(arm_interface.get_pose())
            print(arm_interface.get_reference_frame())
            arm_counter = arm_counter + 1

        # Move each arm on their end-effectors' reference frame
        arm_counter = 1
        for arm_interface in arm_interface_list:
            print("Moving arm {}...".format(arm_counter))
            x = arm_interface.get_pose()
            xd = x * (1 + 0.5 * E_ * i_ * 0.1)
            arm_interface.send_desired_pose(xd)
            arm_interface.send_desired_interpolator_speed(0.1)
            arm_counter = arm_counter + 1
            rclcpp_spin_some(rclcpp_node)  # Spin rclcpp

        rclcpp_shutdown()  # Shutdown rclcpp

    except KeyboardInterrupt:
        print("Interrupted by user")


if __name__ == '__main__':
    main()
