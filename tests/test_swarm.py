import pytest
import numpy as np
from core.robot_agent import RobotAgent
from core.environment import Environment
from core.mesh_node import MeshNode
from core.fault_tolerance import SwarmHealthMonitor
from core.hal_bridge import HALBridge

def test_health_monitor():
    monitor = SwarmHealthMonitor(heartbeat_timeout=0.1)
    agent = RobotAgent(agent_id=0, start_x=2, start_y=2)
    monitor.register_agent(agent.agent_id)
    assert len(monitor.get_active_agents([agent])) == 1

def test_hal_ros2_export():
    agent = RobotAgent(agent_id=0, start_x=2, start_y=2)
    ros_json = HALBridge.export_ros2_occupancy_grid(agent.agent_id, agent.local_map)
    assert "frame_id" in ros_json
    assert "data" in ros_json

def test_environment_obstacles():
    env = Environment()
    assert env.grid[0, 0] == 2
    
