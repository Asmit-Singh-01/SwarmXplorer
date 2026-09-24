import time
import numpy as np
from core.robot_agent import RobotAgent
from core.mesh_node import MeshNode
from config import NUM_AGENTS, MAX_SIMULATION_STEPS, GRID_WIDTH, GRID_HEIGHT, FREE_SPACE

def calculate_global_coverage(agents):
    global_map = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
    for agent in agents:
        global_map = np.maximum(global_map, agent.local_map)
    
    explored = np.sum(global_map == FREE_SPACE)
    total = GRID_WIDTH * GRID_HEIGHT
    return (explored / total) * 100

def handle_p2p_mesh_sync(agents):
    """Checks distances between all agent pairs and merges maps if in communication range."""
    sync_count = 0
    num_a = len(agents)
    for i in range(num_a):
        for j in range(i + 1, num_a):
            if MeshNode.is_in_range(agents[i].position, agents[j].position):
                MeshNode.sync_maps(agents[i], agents[j])
                sync_count += 1
                print(f"   [P2P Mesh Link] Agent {agents[i].agent_id} <---> Agent {agents[j].agent_id} Synced Local Maps!")
    return sync_count

def main():
    print("=" * 60)
    print(" SwarmXplorer - Phase 3: P2P Mesh Communication Engine")
    print("=" * 60)

    agents = [
        RobotAgent(agent_id=0, start_x=2, start_y=2),
        RobotAgent(agent_id=1, start_x=17, start_y=2),
        RobotAgent(agent_id=2, start_x=10, start_y=17)
    ]

    print(f"[*] Initialized Dynamic Mesh Nodes for {NUM_AGENTS} Autonomous Swarm Agents.")

    for step_num in range(1, MAX_SIMULATION_STEPS + 1):
        print(f"\n--- [Step {step_num:02d}/{MAX_SIMULATION_STEPS:02d}] ---")
        
        active_targets = []
        for agent in agents:
            target = agent.step(occupied_targets=active_targets)
            if target:
                active_targets.append(target)
                
            pos = agent.position.tolist()
            coverage = agent.get_explored_percentage()
            print(f" -> Agent {agent.agent_id} | Pos: {pos} | Target: {target} | Knowledge: {coverage:.1f}%")

        # Dynamic Mesh Network Synchronization
        handle_p2p_mesh_sync(agents)

        global_cov = calculate_global_coverage(agents)
        print(f" [*] Swarm Global Exploration Progress: {global_cov:.2f}%")
        time.sleep(0.05)

    print("\n" + "=" * 60)
    print(" P2P Swarm Simulation Run Completed Successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
                                   
