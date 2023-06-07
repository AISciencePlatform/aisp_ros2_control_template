import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sas_robot_kinematics_constrained_multiarm',
            executable='sas_robot_kinematics_constrained_multiarm_node',
            name='sas_robot_kinematics_constrained_multiarm',
            parameters=[{
                "thread_sampling_time_sec": 0.002,
                "n": 40.0,
                "n_d": 6.0,
                "damping": 0.01,
                "damping_secondary": 0.0000001,
                "damping_secondary_labels": ["2_8", "3_8"],
                "alpha": 0.99999,
                "alpha_secondary": 0.99,
                "enable_initial_angle_limit": True,
                "master_device_labels": ["M0_0",
                                         "M0_1",
                                         "M2_1",
                                         "M1_1"],
                "robot_driver_interface_node_prefixes": ["arm1",
                                                         "arm2",
                                                         "arm3",
                                                         "arm4"],
                "robot_kinematics_provider_prefixes": ["arm1_kinematics",
                                                       "arm2_kinematics",
                                                       "arm3_kinematics",
                                                       "arm4_kinematics"],
                "vrep_port": 19998,
                "vrep_ip": os.environ['VREP_IP'],
                "robot_parameter_file_paths": [os.environ['ROBOT_1_JSON_PATH'],
                                               os.environ['ROBOT_2_JSON_PATH'],
                                               os.environ['ROBOT_3_JSON_PATH'],
                                               os.environ['ROBOT_4_JSON_PATH']],
                "vfi_array_yaml_path": os.path.join(
                    get_package_share_directory('aisp_ros2_control_template'), 'cfg', 'vfi_array.yaml')
            }]
        )
    ])
