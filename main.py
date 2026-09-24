import numpy as np
import matplotlib
matplotlib.use('Agg')  # Headless mode for CI/CD
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
GRID_SIZE = (50, 50)
NUM_AGENTS = 3

# --- AGENT LOGIC ---
class RobotAgent:
    def __init__(self, agent_id, start_pos):
        self.agent_id = agent_id
        self.position = np.array(start_pos, dtype=float)

    def step(self):
        # Basic forward movement step
        self.position += np.array([1.0, 1.0])
        return self.position

# --- SIMULATION MAIN ---
def main():
    print("Starting SwarmXplorer Engine...")
    grid_map = np.ones(GRID_SIZE, dtype=int)
    
    agents = [RobotAgent(i, (10 * i + 5, 10 * i + 5)) for i in range(NUM_AGENTS)]
    
    for agent in agents:
        agent.step()
        
    # Render Output
    plt.figure(figsize=(6, 6))
    plt.imshow(grid_map, cmap='binary')
    for agent in agents:
        plt.scatter(agent.position[1], agent.position[0], label=f"Agent {agent.agent_id}")
    plt.title("SwarmXplorer Simulation")
    plt.savefig("simulation_output.png")
    plt.close()

    print("Simulation completed successfully. Image saved to simulation_output.png")

if __name__ == "__main__":
    main()
