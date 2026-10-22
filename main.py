import os
import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, FREE_SPACE, OBSTACLE, UNEXPLORED
from core.robot_agent import RobotAgent
from core.sensor_fusion import SensorNoiseFilter
from algos.market_auction import MarketAuction
from core.telemetry_logger import SwarmTelemetryLogger

def run_swarm_simulation(max_steps=5):
    print("🚀 Initializing SwarmXplorer Enterprise Orchestration Engine...")
    
    # Initialize Environment Grid
    env_grid = np.full((GRID_HEIGHT, GRID_HEIGHT), FREE_SPACE, dtype=int)
    env_grid[5:15, 10:12] = OBSTACLE 
    
    # Initialize Heterogeneous Swarm Agents
    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2, capability="AIR"),
        RobotAgent(agent_id=1, start_x=2, start_y=18, capability="LAND"),
        RobotAgent(agent_id=2, start_x=18, start_y=2, capability="UNDERGROUND")
    ]
    
    telemetry = SwarmTelemetryLogger(log_dir="logs")
    
    for step in range(max_steps):
        all_frontiers = [[10, 5], [15, 15], [5, 15]]
        
        # Run Market Auction
        allocations = MarketAuction.run_auction(agents, all_frontiers)
        
        # Execute Agent Steps
        for agent in agents:
            assigned_target = allocations.get(agent.agent_id)
            noisy_dist = SensorNoiseFilter.add_lidar_noise(4.0)
            smoothed_state, _ = SensorNoiseFilter.kalman_filter_step(3.8, noisy_dist, 0.2)
            
            target_pos = list(assigned_target) if assigned_target else agent.position.tolist()
            agent.step(env_grid, agents, assigned_target=target_pos)
            
        # Global Coverage
        total_explored = sum(np.sum(a.local_map != UNEXPLORED) for a in agents)
        global_coverage = (total_explored / (GRID_WIDTH * GRID_HEIGHT * len(agents))) * 100
        
        telemetry.log_step(step_num=step+1, agents=agents, global_coverage=global_coverage, leader_id=0)

    log_path = telemetry.save_to_disk()
    print(f"✅ Mission simulation complete. Telemetry saved to: {log_path}")
    return log_path

if __name__ == "__main__":
    run_swarm_simulation()
