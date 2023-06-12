#include <rclcpp/rclcpp.hpp>
#include <sas_core/sas_clock.hpp>
#include <sas_robot_kinematics/sas_robot_kinematics_client.hpp>

#include<signal.h>
static std::atomic_bool kill_this_process(false);
void sig_int_handler(int)
{
    kill_this_process = true;
}


int main(int argc, char** argv)
{
    if(signal(SIGINT, sig_int_handler) == SIG_ERR)
    {
        throw std::runtime_error("::Error setting the signal int handler.");
    }

    rclcpp::init(argc,argv,rclcpp::InitOptions(),rclcpp::SignalHandlerOptions::None);
    auto node = std::make_shared<rclcpp::Node>("aisp_ros2_kinematics_control_example_cpp");

    try
    {

        auto arm_interface_list = {std::make_shared<sas::RobotKinematicsClient>(node,"arm1_kinematics"),
                                   std::make_shared<sas::RobotKinematicsClient>(node,"arm2_kinematics"),
                                   std::make_shared<sas::RobotKinematicsClient>(node,"arm3_kinematics"),
                                   std::make_shared<sas::RobotKinematicsClient>(node,"arm4_kinematics")};

        bool all_interfaces_enabled = false;
        while(not all_interfaces_enabled)
        {
            rclcpp::spin_some(node);
            all_interfaces_enabled = true;
            for(const auto& arm_interface: arm_interface_list)
            {
                if (not arm_interface->is_enabled())
                {
                    all_interfaces_enabled=false;
                    break;
                }
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
        }

        int arm_counter = 1;
        for(const auto& arm_interface : arm_interface_list)
        {
            RCLCPP_INFO_STREAM(node->get_logger(),"****************************");
            RCLCPP_INFO_STREAM(node->get_logger(),"***Initial info for arm " << arm_counter << "...");
            RCLCPP_INFO_STREAM(node->get_logger(),"****************************");
            RCLCPP_INFO_STREAM(node->get_logger(),arm_interface->get_pose());
            RCLCPP_INFO_STREAM(node->get_logger(),arm_interface->get_reference_frame());
            arm_counter++;
        }

        // Move each arm on their end-effectors' reference frame
        arm_counter = 1;
        for(const auto& arm_interface : arm_interface_list)
        {
            RCLCPP_INFO_STREAM(node->get_logger(),"Moving arm "  << arm_counter << "...");
            DQ x = arm_interface->get_pose();
            DQ xd = x * (1 + 0.5 * E_ * i_ * 0.1);
            arm_interface->send_desired_pose(xd);
            arm_interface->send_desired_interpolator_speed(0.1);
            arm_counter++;
            rclcpp::spin_some(node);
        }

    }
    catch (const std::exception& e)
    {
        RCLCPP_ERROR_STREAM(node->get_logger(),std::string("::Exception::") + e.what());
    }

    return 0;
}

