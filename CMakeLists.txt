cmake_minimum_required(VERSION 3.8)
project(aisp_ros2_control_template)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sas_core REQUIRED)
find_package(sas_common REQUIRED)
find_package(sas_conversions REQUIRED)
find_package(sas_robot_driver REQUIRED)
find_package(sas_robot_kinematics REQUIRED)
find_package(sas_robot_kinematics_constrained_multiarm REQUIRED)
find_package(Eigen3 REQUIRED)

##### CPP BINARY #####

add_executable(aisp_control_example_cpp
    src/aisp_ros2_control_template_cpp.cpp)

ament_target_dependencies(aisp_control_example_cpp
    rclcpp
    geometry_msgs
    std_msgs
    sas_msgs
    sas_common
    sas_core
    sas_conversions
    sas_robot_driver
    sas_robot_kinematics
    sas_robot_kinematics_constrained_multiarm)

install(TARGETS
  aisp_control_example_cpp
  DESTINATION lib/${PROJECT_NAME})

##END## CPP BINARY #####

##### PYTHON EXECUTABLES #####
install(PROGRAMS
  scripts/aisp_control_example_py.py
  DESTINATION lib/${PROJECT_NAME}
)
##END## PYTHON EXECUTABLES #####

##### CFG FILES #####

install(DIRECTORY
  cfg
  DESTINATION cfg/${PROJECT_NAME}/
)

##END## CFG FILES #####

##### LAUNCH FILES #####

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

##END## LAUNCH FILES #####

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
