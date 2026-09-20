import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from core.robot_agent import RobotAgent
from sim.visualizer import save_swarm_map

def main():
    print("Initializing SwarmXplorer System...")
    bots = [RobotAgent(bot_id=i) for i in range(config.NUM_ROBOTS)]
    
    print(f"Running simulation with {len(bots)} agents...")
    for step in range(config.SIMULATION_STEPS):
        for bot in bots:
            if hasattr(bot, 'step'):
                bot.step(bots)
                
    print("Saving map output...")
    save_swarm_map(bots)
    print("Simulation completed successfully!")

if __name__ == "__main__":
    main()
    
