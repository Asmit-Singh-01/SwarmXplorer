import time
import numpy as np
from core.robot_agent import RobotAgent
from config import NUM_AGENTS, MAX_SIMULATION_STEPS, GRID_WIDTH, GRID_HEIGHT, FREE_SPACE

def calculate_global_coverage(agents):
    # Merge all individual local maps to get overall swarm progress
    global_map = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    for agent in agents:
        global_map = np.maximum(global_map, agent.local_map)
    
    explored = np.sum(global_map == FREE_SPACE)
    total = GRID_WIDTH * GRID_HEIGHT
    return (explored / total) * 100

def main():
    print("=" * 60)
    print(" SwarmXplorer - Phase 2: Multi-Agent Frontier Exploration")
    print("=" * 60)

    # Spawn 3 agents at different arena quadrants
    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2),
        RobotAgent(agent_id=1, start_x=17, start_y=2),
        RobotAgent(agent_id=2, start_x=10, start_y=17)
    ]

    print(f"[*] Initialized Swarm with {NUM_AGENTS} Decentralized Nodes.")

    for step_num in range(1, MAX_SIMULATION_STEPS + 1):
        print(f"\n--- [Step {step_num:02d}/{MAX_SIMULATION_STEPS:02d}] ---")
        
        active_targets = []
        for agent in agents:
            target = agent.step(occupied_targets=active_targets)
            if target:
                active_targets.append(target)
                
            pos = agent.position.tolist()
            coverage = agent.get_explored_percentage()
            print(f" -> Agent {agent.agent_id} | Pos: {pos} | Target: {target} | Local Coverage: {coverage:.1f}%")

        global_cov = calculate_global_coverage(agents)
        print(f" [*] Swarm Global Exploration Progress: {global_cov:.2f}%")
        time.sleep(0.05)

    print("\n" + "=" * 60)
    print(" Swarm Exploration Run Completed Successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
    
