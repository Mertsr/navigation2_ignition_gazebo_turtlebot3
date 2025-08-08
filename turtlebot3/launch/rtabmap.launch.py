    
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=['/home/mertsrc/ros2_ws/src/navigation2_ignition_gazebo_turtlebot3/turtlebot3/config/rtabmap_params.yaml'],
            remappings=[
                ('odom', '/odom'),
                ('rgb/image', '/camera/rgb/image_raw'),
                ('rgb/camera_info', '/camera/rgb/camera_info'),
                ('depth/image', '/camera/depth/image_raw'),
            ]
        ),
    ])
