# This launchfile is meant to be used as a part of a vscode task.
# For using it outside of this task remember to export and source all the necessary files
# as in "nav2_sim_launch.sh" script.


from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch.actions import ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, FindExecutable


def generate_launch_description():
    rosbag2_snapshot_node = Node(
        package="rosbag2_snapshot",
        executable="snapshotter",
        namespace="robo_cart",
        parameters=[
            PathJoinSubstitution(
                [
                    FindPackageShare("rosbag2_snapshot"),
                    "param",
                    "multiple_topics.params.yaml",
                ]
            ),
        ],
        output="screen",
        emulate_tty=True,
        respawn=True,
        respawn_delay=2.0,
    )

    actions = [
        rosbag2_snapshot_node,
    ]
    return LaunchDescription(actions)
