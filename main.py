from sim.visualizer import save_swarm_map
from core.robot_agent import RobotAgent
import config

if __name__ == "__main__":
    # Initialize agents
    bots = [RobotAgent(bot_id=i) for i in range(config.NUM_ROBOTS)]
    
    # Run simulation iterations
    for step in range(config.SIMULATION_STEPS):
        for bot in bots:
            bot.step(bots)
            
    # Save output visualization
    save_swarm_map(bots)
    print("Simulation completed successfully.")
    
