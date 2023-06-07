import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
   sim_aisp_cobotta_1 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('aisp_ros2_control_template'), 'launch'),
         '/sim_aisp_cobotta_1_launch.py'])
      )
   sim_aisp_cobotta_2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('aisp_ros2_control_template'), 'launch'),
         '/sim_aisp_cobotta_2_launch.py'])
      )
   sim_aisp_vs050_1 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('aisp_ros2_control_template'), 'launch'),
         '/sim_aisp_vs050_1_launch.py'])
      )
   sim_aisp_vs050_2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('aisp_ros2_control_template'), 'launch'),
         '/sim_aisp_vs050_2_launch.py'])
      )
   sas_robot_kinematics_constrained_multiarm = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('aisp_ros2_control_template'), 'launch'),
         '/sas_robot_kinematics_constrained_multiarm_launch.py'])
      )

   return LaunchDescription([
      sim_aisp_cobotta_1,
      sim_aisp_cobotta_2,
      sim_aisp_vs050_1,
      sim_aisp_vs050_2,
      sas_robot_kinematics_constrained_multiarm
   ])
