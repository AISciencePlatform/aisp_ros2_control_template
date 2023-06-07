import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sas_robot_driver',
            executable='sas_robot_driver_ros_composer_node',
            name='arm2',
            parameters=[{
                "use_real_robot": False,
                "use_coppeliasim": True,
                "robot_driver_client_names": ["EMPTY_LIST"],
                "override_joint_limits_with_robot_parameter_file": True,
                "thread_sampling_time_sec": 0.001,
                "vrep_port": 20011,
                "vrep_dynamically_enabled": True,
                "vrep_robot_joint_names": ["Cobotta1_rjointb",
                                           "Cobotta1_pjointb",
                                           "Cobotta1_rjoint1",
                                           "Cobotta1_rjoint2",
                                           "Cobotta1_rjoint3",
                                           "Cobotta1_rjoint4",
                                           "Cobotta1_rjoint5",
                                           "Cobotta1_rjoint6"],
                "vrep_ip": os.environ['VREP_IP'],
                "robot_parameter_file_path": os.environ['ROBOT_2_JSON_PATH']
            }]
        )
    ])
