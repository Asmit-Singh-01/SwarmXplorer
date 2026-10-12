import time
import numpy as np
from core.environment import Environment
from core.robot_agent import RobotAgent
from core.mesh_node import MeshNode
from core.analytics import SwarmAnalytics
from core.fault_tolerance import SwarmHealthMonitor
from core.hal_bridge import HALBridge
from algos.leader_election import LeaderElection
from config import NUM_AGENTS, MAX_SIMULATION_STEPS, GRID_WIDTH, GRID_HEIGHT, UNEXPLORED

def get_merged_global_map(agents):
    global_map = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    for agent in agents:
        global_map = np.maximum(global_map, agent.local_map)
    return global_map

def calculate_global_coverage(global_map):
    explored = np.sum(global_map != UNEXPLORED)
    total = GRID_WIDTH * GRID_HEIGHT
    return (explored / total) * 100

def main():
    print("=" * 65)
    print(" SwarmXplorer - Advanced Flocking & Formation Control Engine")
    print("=" * 65)

    env = Environment()
    health_monitor = SwarmHealthMonitor(heartbeat_timeout=2.0)

    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2),
        RobotAgent(agent_id=1, start_x=17, start_y=2),
        RobotAgent(agent_id=2, start_x=2, start_y=17)
    ]

    for agent in agents:
        health_monitor.register_agent(agent.agent_id)

    for step_num in range(1, MAX_SIMULATION_STEPS + 1):
        for agent in agents:
            health_monitor.update_heartbeat(agent.agent_id)

        active_agents = health_monitor.get_active_agents(agents)
        current_leader = LeaderElection.elect_leader(active_agents)

        active_targets = []
        for agent in active_agents:
            target = agent.step(env.grid, active_agents, occupied_targets=active_targets)
            if target:
                active_targets.append(target)
            
            _ = HALBridge.export_ros2_occupancy_grid(agent.agent_id, agent.local_map)

        num_a = len(active_agents)
        for i in range(num_a):
            for j in range(i + 1, num_a):
                if MeshNode.is_in_range(active_agents[i].position, active_agents[j].position):
                    MeshNode.sync_maps(active_agents[i], active_agents[j])

        global_map = get_merged_global_map(active_agents)
        coverage = calculate_global_coverage(global_map)
        
        leader_id = current_leader.agent_id if current_leader else "None"
        print(f"[*] Step {step_num:02d} | Coordinator: Agent {leader_id} | Coverage: {coverage:.2f}%")

    SwarmAnalytics.print_performance_report(agents, coverage)

if __name__ == "__main__":
    main()
    
