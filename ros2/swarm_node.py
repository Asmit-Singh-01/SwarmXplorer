import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

class SwarmROS2Node(Node):
    """
    Official ROS 2 Node wrapper for SwarmXplorer autonomous agents,
    communicating via standard /cmd_vel and /map topics.
    """
    def __init__(self, agent_id):
        super().__init__(f'swarm_agent_node_{agent_id}')
        self.agent_id = agent_id
        
        # Publishers for velocity commands and telemetry maps
        self.cmd_publisher = self.create_publisher(Twist, f'/agent_{agent_id}/cmd_vel', 10)
        self.map_publisher = self.create_publisher(OccupancyGrid, f'/agent_{agent_id}/map', 10)
        
        self.get_logger().info(f"[ROS2] Swarm Agent Node {agent_id} successfully initialized & online.")

    def publish_velocity(self, linear_x, angular_z):
        twist = Twist()
        twist.linear.x = float(linear_x)
        twist.angular.z = float(angular_z)
        self.cmd_publisher.publish(twist)

    def publish_local_map(self, local_map_matrix):
        msg = OccupancyGrid()
        msg.header.frame_id = f"agent_{self.agent_id}_link"
        msg.info.width = local_map_matrix.shape[1]
        msg.info.height = local_map_matrix.shape[0]
        msg.info.resolution = 1.0
        msg.data = local_map_matrix.flatten().tolist()
        self.map_publisher.publish(msg)
