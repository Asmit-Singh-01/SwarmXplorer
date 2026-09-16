import time
from core.robot_agent import SwarmAgent
from config import ARENA_WIDTH, ARENA_HEIGHT

def run_simulation(steps=50):
    print("--- SwarmXplorer Simulation Starting ---")
    
    # Initialize 3 Swarm Agents at center
    bots = [
        SwarmAgent(0, 400, 300),
        SwarmAgent(1, 410, 305),
        SwarmAgent(2, 390, 295)
    ]

    for step_num in range(1, steps + 1):
        all_positions = {bot.id: bot.position for bot in bots}
        
        for bot in bots:
            bot.step(all_positions)
            
        if step_num % 10 == 0:
            print(f"Step {step_num}:")
            for bot in bots:
                print(f"  Robot {bot.id} Pos: [{bot.position[0]:.1f}, {bot.position[1]:.1f}] | Active Mesh Links: {bot.mesh.neighbors}")

if __name__ == "__main__":
    run_simulation()
    
