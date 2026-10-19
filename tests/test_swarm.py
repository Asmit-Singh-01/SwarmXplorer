import pytest
import numpy as np
from core.robot_agent import RobotAgent
from core.environment import Environment
from core.mesh_node import MeshNode
from core.fault_tolerance import SwarmHealthMonitor
from core.hal_bridge import HALBridge
from algos.leader_election import LeaderElection
from core.physics_model import DifferentialDrivePhysics

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
from algos.market_auction import MarketAuction

def test_market_auction():
    agent = RobotAgent(agent_id=0, start_x=2, start_y=2)
    frontiers = [(5, 5), (10, 10)]
    
    allocations = MarketAuction.run_auction([agent], frontiers)
    assert agent.agent_id in allocations
    assert allocations[agent.agent_id] in frontiers


from core.physics_model import DifferentialDrivePhysics

def test_differential_drive_physics():
    physics = DifferentialDrivePhysics(max_linear_speed=2.0)
    start = [0, 0]
    target = [3, 4]
    
    next_pos = physics.compute_kinematic_step(start, target, dt=1.0)
    assert len(next_pos) == 2
    # Verify that the agent moved correctly towards the target on the grid
    assert next_pos[0] >= start[0]
    assert next_pos[1] >= start[1]
import os

def test_docker_config_exists():
    assert os.path.exists("Dockerfile")
    assert os.path.exists("docker-compose.yml")
from core.voxel_grid_3d import VoxelGrid3D
from core.sensor_fusion import SensorNoiseFilter

def test_voxel_grid_3d():
    voxel_world = VoxelGrid3D(width=10, height=10, depth=5)
    voxel_world.update_voxel(2, 3, 1, 2) # Set obstacle
    sub_vol = voxel_world.get_local_volume((2, 3, 1), radius=1)
    assert sub_vol.shape[0] > 0
    assert 2 in sub_vol

def test_sensor_noise_and_kalman():
    true_dist = 5.0
    noisy_measurement = SensorNoiseFilter.add_lidar_noise(true_dist, noise_level=0.1)
    
    # Run through Kalman filter
    smoothed_state, _ = SensorNoiseFilter.kalman_filter_step(
        estimated_state=4.8, 
        measurement=noisy_measurement, 
        covariance=0.5
    )
    assert isinstance(smoothed_state, float)


