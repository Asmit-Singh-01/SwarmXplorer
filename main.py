import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, FREE_SPACE, OBSTACLE, UNEXPLORED
from core.robot_agent import RobotAgent
from core.sensor_fusion import SensorNoiseFilter
from algos.market_auction import MarketAuction
from algos.mapf_cbs import MAPFEngine
from algos.velocity_obstacles import VelocityObstacles
from core.telemetry_logger import SwarmTelemetryLogger

def run_swarm_simulation(max_steps=50):
    print("🚀 Initializing SwarmXplorer Enterprise Orchestration Engine...")
    
    # Initialize Environment Grid (Simple test map with obstacles)
    env_grid = np.full((GRID_HEIGHT, GRID_WIDTH), FREE_SPACE, dtype=int)
    env_grid[5:15, 10:12] = OBSTACLE # Add a structural obstacle wall
    
    # Initialize Heterogeneous Swarm Agents
    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2, capability="AIR"),
        RobotAgent(agent_id=1, start_x=2, start_y=18, capability="LAND"),
        RobotAgent(agent_id=2, start_x=18, start_y=2, capability="UNDERGROUND")
    ]
    
    telemetry = SwarmTelemetryLogger(log_dir="logs")
    
    for step in range(max_steps):
        print(f"\n--- Simulation Step [{step + 1}/{max_steps}] ---")
        
        # 1. Collect all agent local frontiers or exploration targets
        all_frontiers = [[10, 5], [15, 15], [5, 15], [12, 8]]
        
        # 2. Run Capability-Aware Market Auction
        allocations = MarketAuction.run_auction(agents, all_frontiers)
        
        # 3. Execute Agent Steps with Sensor Noise & Collision Avoidance
        for agent in agents:
            assigned_target = allocations.get(agent.agent_id)
            
            # Simulate Sensor Noise & Filtering
            noisy_dist = SensorNoiseFilter.add_lidar_noise(4.0)
            smoothed_state, _ = SensorNoiseFilter.kalman_filter_step(3.8, noisy_dist, 0.2)
            
            # Step agent using orchestrator logic
            target_pos = assigned_target if assigned_target else agent.position
            agent.step(env_grid, agents, assigned_target=target_pos)
            
        # 4. Calculate Global Coverage
        total_explored = sum(np.sum(a.local_map != UNEXPLORED) for a in agents)
        global_coverage = (total_explored / (GRID_WIDTH * GRID_HEIGHT * len(agents))) * 100
        
        # 5. Log Telemetry
        telemetry.log_step(step_num=step+1, agents=agents, global_coverage=global_coverage, leader_id=0)
        print(f"Global Coverage: {global_coverage:.2f}% | Active Allocations: {allocations}")

    # Save Blackbox Mission Log
    log_path = telemetry.save_to_disk()
    print(f"\n✅ Mission simulation complete. Telemetry saved to: {log_path}")

if __name__ == "__main__":
    run_swarm_simulation()
