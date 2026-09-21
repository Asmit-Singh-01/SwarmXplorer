import numpy as np
from core.robot_agent import RobotAgent
from sim.visualizer import render_swarm
from config import NUM_AGENTS, GRID_SIZE

def main():
    print("Starting SwarmXplorer Engine...")
    grid_map = np.ones(GRID_SIZE, dtype=int)
    
    # Initialize agents
    agents = [RobotAgent(i, (10 * i + 5, 10 * i + 5)) for i in range(NUM_AGENTS)]
    
    # Run simulation step
    for agent in agents:
        agent.step()
        
    render_swarm(agents, grid_map)
    print("Simulation completed successfully. Output saved to simulation_output.png")

if __name__ == "__main__":
    main()
    
