import sys
import os

# Project root add karo taaki import error kabhi na aaye
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from core.robot_agent import RobotAgent
from sim.visualizer import save_swarm_map

def main():
    print("Initializing SwarmXplorer System...")
    bots = [RobotAgent(bot_id=i) for i in range(config.NUM_ROBOTS)]
    
    print(f"Running simulation for {config.SIMULATION_STEPS} steps...")
    for step in range(config.SIMULATION_STEPS):
        for bot in bots:
            if hasattr(bot, 'step'):
                bot.step(bots)
                
    save_swarm_map(bots)
    print("Simulation finished successfully!")

if __name__ == "__main__":
    main()
    
