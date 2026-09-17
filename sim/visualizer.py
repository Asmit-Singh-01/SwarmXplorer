import matplotlib.pyplot as plt
import numpy as np

def save_swarm_map(bots, filename="swarm_exploration_map.png"):
    """Generates and saves a visual map of the swarm's coverage and mesh connectivity."""
    plt.figure(figsize=(8, 6))
    
    # Merge all occupancy maps into a global view
    global_map = np.zeros_like(bots[0].grid_map)
    for bot in bots:
        global_map = np.maximum(global_map, bot.grid_map)
    
    # Plot explored territory
    plt.imshow(global_map.T, cmap='Blues', origin='lower', extent=[0, 800, 0, 600], alpha=0.6)
    
    # Plot active Mesh Links between connected robots
    for i, bot_a in enumerate(bots):
        for bot_b in bots:
            if bot_b.id in bot_a.mesh.neighbors:
                plt.plot([bot_a.position[0], bot_b.position[0]], 
                         [bot_a.position[1], bot_b.position[1]], 
                         'g--', alpha=0.5, label='Mesh Link' if i == 0 else "")
    
    # Plot Robots
    for bot in bots:
        plt.scatter(bot.position[0], bot.position[1], color='red', s=100, zorder=5)
        plt.text(bot.position[0] + 10, bot.position[1] + 10, f"Bot {bot.id}", fontsize=10, weight='bold')

    plt.title("SwarmXplorer: Decentralized Coverage & Dynamic Mesh Network")
    plt.xlabel("X Coordinate (m)")
    plt.ylabel("Y Coordinate (m)")
    plt.xlim(0, 800)
    plt.ylim(0, 600)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Save image to repository root
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Map visualization successfully saved to {filename}")
          
