import matplotlib
matplotlib.use('Agg')  # Display-less background mode for CI/CD
import matplotlib.pyplot as plt

def render_swarm(agents, grid_map):
    plt.figure(figsize=(6, 6))
    plt.imshow(grid_map, cmap='binary')
    for agent in agents:
        plt.scatter(agent.position[1], agent.position[0], label=f"Agent {agent.agent_id}")
    plt.title("SwarmXplorer Simulation")
    plt.savefig("simulation_output.png")
    plt.close()
    
