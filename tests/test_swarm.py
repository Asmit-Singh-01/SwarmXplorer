import pytest
import numpy as np
from core.robot_agent import RobotAgent
from core.environment import Environment
from core.mesh_node import MeshNode
from core.fault_tolerance import SwarmHealthMonitor
from core.hal_bridge import HALBridge
from algos.leader_election import LeaderElection

def test_agent_initialization():
    agent = RobotAgent(agent_id=0, start_x=2, start_y=2)
    assert agent.agent_id == 0
    assert np.array_equal(agent.position, np.array([2, 2]))

def test_mesh_consensus():
    agent_a = RobotAgent(agent_id=0, start_x=2, start_y=2)
    agent_b = RobotAgent(agent_id=1, start_x=3, start_y=2)

    agent_a.local_map[5, 5] = 1
    agent_b.local_map[8, 8] = 1

    MeshNode.sync_maps(agent_a, agent_b)

    assert agent_a.local_map[5, 5] == 1
    assert agent_a.local_map[8, 8] == 1
    assert agent_b.local_map[5, 5] == 1
    assert agent_b.local_map[8, 8] == 1

def test_environment_obstacles():
    env = Environment()
    assert env.grid[0, 0] == 2

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

def test_leader_election():
    agent_low = RobotAgent(agent_id=1, start_x=2, start_y=2)
    agent_high = RobotAgent(agent_id=5, start_x=5, start_y=5)
    
    active_agents = [agent_low, agent_high]
    leader = LeaderElection.elect_leader(active_agents)
    
    assert leader.agent_id == 5
    
