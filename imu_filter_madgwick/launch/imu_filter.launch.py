import os
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_dir = os.path.join(get_package_share_directory('imu_filter_madgwick'), 'config','imu_filter.yaml')
    
    use_mag_arg = DeclareLaunchArgument(
        'use_mag',
        default_value='False',
        description='Use magnetometer data'
    )


    return launch.LaunchDescription(
        [   
            use_mag_arg,
            launch_ros.actions.Node(
                package='imu_filter_madgwick',
                executable='imu_filter_madgwick_node',
                name='imu_filter',
                output='screen',
                # parameters=[config_dir, {'use_mag': LaunchConfiguration('use_mag')}],
                parameters=[config_dir, {'use_mag': LaunchConfiguration('use_mag')}],

            ),
        ]
    )