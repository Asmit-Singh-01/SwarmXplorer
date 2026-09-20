import os
import sys

# Set root project path for python module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from core.robot_agent import RobotAgent
from sim.visualizer import save_swarm_map

def main():
    print("Initializing SwarmXplorer System...")
    
    bots = [RobotAgent(bot_id=i) for i in range(config.NUM_ROBOTS)]
    
    print(f"Starting Swarm Simulation with {len(bots)} agents for {config.SIMULATION_STEPS} steps...")
    
    for step in range(config.SIMULATION_STEPS):
        for bot in bots:
            if hasattr(bot, 'step'):
                bot.step(bots)
            elif hasattr(bot, 'update'):
                bot.update(bots)
                
    print("Simulation completed successfully. Generating exploration map...")
    save_swarm_map(bots)

if __name__ == "__main__":
    main()
    
