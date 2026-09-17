import time
import numpy as np
from core.robot_agent import SwarmAgent
from sim.visualizer import save_swarm_map

def run_simulation(steps=150):
    print("--- SwarmXplorer: Starting Visual Swarm Test ---")
    
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
            
        if step_num % 30 == 0:
            print(f"[Step {step_num}] Active Connections: {[bot.mesh.neighbors for bot in bots]}")

    # Generate Image Artifact
    save_swarm_map(bots, "swarm_exploration_map.png")

if __name__ == "__main__":
    run_simulation()
    
