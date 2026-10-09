import json

class HALBridge:
    """
    Hardware Abstraction Layer to translate swarm state into standard ROS 2 message format.
    """
    @staticmethod
    def export_ros2_occupancy_grid(agent_id, local_map):
        """Formats map into standard nav_msgs/OccupancyGrid structure."""
        ros_map_msg = {
            "header": {
                "frame_id": "map",
                "agent_id": agent_id
            },
            "info": {
                "width": local_map.shape[1],
                "height": local_map.shape[0],
                "resolution": 1.0
            },
            "data": local_map.flatten().tolist()
        }
        return json.dumps(ros_map_msg)

    @staticmethod
    def export_cmd_vel(agent_id, velocity_vector):
        """Formats motor velocity into geometry_msgs/Twist structure."""
        twist_msg = {
            "agent_id": agent_id,
            "linear": {"x": float(velocity_vector[0]), "y": float(velocity_vector[1]), "z": 0.0},
            "angular": {"x": 0.0, "y": 0.0, "z": 0.0}
        }
        return twist_msg
      
