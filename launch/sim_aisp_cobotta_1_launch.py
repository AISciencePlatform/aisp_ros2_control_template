import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sas_robot_driver',
            executable='sas_robot_driver_ros_composer_node',
            name='arm1',
            parameters=[{
                "use_real_robot": False,
                "use_coppeliasim": True,
                "robot_driver_client_names": ["EMPTY_LIST"],
                "override_joint_limits_with_robot_parameter_file": True,
                "thread_sampling_time_sec": 0.001,
                "vrep_port": 20010,
                "vrep_dynamically_enabled": True,
                "vrep_robot_joint_names": ["Cobotta2_rjointb",
                                           "Cobotta2_pjointb",
                                           "Cobotta2_rjoint1",
                                           "Cobotta2_rjoint2",
                                           "Cobotta2_rjoint3",
                                           "Cobotta2_rjoint4",
                                           "Cobotta2_rjoint5",
                                           "Cobotta2_rjoint6"],
                "vrep_ip": os.environ['VREP_IP'],
                "robot_parameter_file_path": os.environ['ROBOT_1_JSON_PATH']
            }]
        )
    ])
