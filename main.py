import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sim.visualizer import save_swarm_map
from core.robot_agent import RobotAgent
import config

if __name__ == "__main__":
    bots = [RobotAgent(bot_id=i) for i in range(config.NUM_ROBOTS)]
    
    for step in range(config.SIMULATION_STEPS):
        for bot in bots:
            bot.step(bots)
            
    save_swarm_map(bots)
    print("Simulation completed successfully.")
    
