import time
import numpy as np
from core.robot_agent import SwarmAgent

def run_simulation(steps=100):
    print("--- SwarmXplorer: Starting Decentralized Swarm Test ---")
    
    # Initialize 3 Swarm Agents
    bots = [
        SwarmAgent(0, 400, 300),
        SwarmAgent(1, 410, 305),
        SwarmAgent(2, 390, 295)
    ]

    agents_dict = {bot.id: bot for bot in bots}

    for step_num in range(1, steps + 1):
        all_positions = {bot.id: bot.position for bot in bots}
        
        for bot in bots:
            bot.step(all_positions, agents_dict)
            
        if step_num % 20 == 0:
            print(f"\n[Step {step_num}] Swarm Mesh Status:")
            for bot in bots:
                explored_cells = int(np.sum(bot.grid_map))
                print(f"  Robot {bot.id} | Pos: [{bot.position[0]:.1f}, {bot.position[1]:.1f}] | Links: {bot.mesh.neighbors} | Explored Cells: {explored_cells}")

    # Calculate Global Merged Map Coverage
    global_map = np.zeros_like(bots[0].grid_map)
    for bot in bots:
        global_map = np.maximum(global_map, bot.grid_map)
    
    total_coverage = (np.sum(global_map) / global_map.size) * 100
    print(f"\n==========================================")
    print(f"Total Arena Coverage Achieved: {total_coverage:.2f}%")
    print(f"==========================================")

if __name__ == "__main__":
    run_simulation()
    
