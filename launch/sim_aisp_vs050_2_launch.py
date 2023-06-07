import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sas_robot_driver',
            executable='sas_robot_driver_ros_composer_node',
            name='arm4',
            parameters=[{
                "use_real_robot": False,
                "use_coppeliasim": True,
                "robot_driver_client_names": ["EMPTY_LIST"],
                "override_joint_limits_with_robot_parameter_file": True,
                "thread_sampling_time_sec": 0.001,
                "vrep_port": 20013,
                "vrep_dynamically_enabled": True,
                "vrep_robot_joint_names": ["Denso2_VS050_rjointb",
                                           "Denso2_VS050_pjointb",
                                           "Denso2_VS050_rjoint1",
                                           "Denso2_VS050_rjoint2",
                                           "Denso2_VS050_rjoint3",
                                           "Denso2_VS050_rjoint4",
                                           "Denso2_VS050_rjoint5",
                                           "Denso2_VS050_rjoint6",
                                           "Denso2_VS050_rjoint7_tool"],
                "vrep_ip": os.environ['VREP_IP'],
                "robot_parameter_file_path": os.environ['ROBOT_4_JSON_PATH']
            }]
        )
    ])
