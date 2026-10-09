import time
import numpy as np
from core.environment import Environment
from core.robot_agent import RobotAgent
from core.mesh_node import MeshNode
from core.renderer import TerminalRenderer
from core.analytics import SwarmAnalytics
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

def handle_p2p_mesh_sync(agents):
    num_a = len(agents)
    for i in range(num_a):
        for j in range(i + 1, num_a):
            if MeshNode.is_in_range(agents[i].position, agents[j].position):
                MeshNode.sync_maps(agents[i], agents[j])

def main():
    print("=" * 60)
    print(" SwarmXplorer - Advanced Path-Planning Swarm Engine")
    print("=" * 60)

    env = Environment()
    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2),
        RobotAgent(agent_id=1, start_x=17, start_y=2),
        RobotAgent(agent_id=2, start_x=2, start_y=17)
    ]

    for step_num in range(1, MAX_SIMULATION_STEPS + 1):
        active_targets = []
        for agent in agents:
            target = agent.step(env.grid, occupied_targets=active_targets)
            if target:
                active_targets.append(target)

        handle_p2p_mesh_sync(agents)
        global_map = get_merged_global_map(agents)
        coverage = calculate_global_coverage(global_map)
        print(f"[*] Step {step_num:02d}/{MAX_SIMULATION_STEPS:02d} | Global Coverage: {coverage:.2f}%")

    # Render Terminal Grid and Analytics
    print("\n[+] Final Arena Knowledge Base:")
    TerminalRenderer.render(global_map, agents)
    SwarmAnalytics.print_performance_report(agents, coverage)

if __name__ == "__main__":
    main()
    
