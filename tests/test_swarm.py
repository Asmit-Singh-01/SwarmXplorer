import pytest
import numpy as np
from core.robot_agent import RobotAgent
from core.environment import Environment
from core.mesh_node import MeshNode

def test_agent_initialization():
    agent = RobotAgent(agent_id=0, start_x=2, start_y=2)
    assert agent.agent_id == 0
    assert np.array_equal(agent.position, np.array([2, 2]))

def test_mesh_consensus():
    agent_a = RobotAgent(agent_id=0, start_x=2, start_y=2)
    agent_b = RobotAgent(agent_id=1, start_x=3, start_y=2)

    # Force distinct map states
    agent_a.local_map[5, 5] = 1
    agent_b.local_map[8, 8] = 1

    # Sync
    MeshNode.sync_maps(agent_a, agent_b)

    # Verify both maps are identical and contain both discovered points
    assert agent_a.local_map[5, 5] == 1
    assert agent_a.local_map[8, 8] == 1
    assert agent_b.local_map[5, 5] == 1
    assert agent_b.local_map[8, 8] == 1

def test_environment_obstacles():
    env = Environment()
    assert env.grid[0, 0] == 2  # Perimeter Wall check
