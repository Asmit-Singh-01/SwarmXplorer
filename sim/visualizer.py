import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def save_swarm_map(bots, filename="swarm_exploration_map.png"):
    plt.figure(figsize=(8, 8))
    
    for bot in bots:
        # Plot robot positions
        pos = getattr(bot, 'position', (0, 0))
        plt.scatter(pos[0], pos[1], label=f"Robot {getattr(bot, 'id', 0)}")
        
    plt.title("SwarmXplorer - Real-time Swarm Mapping")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    
    # Save output plot
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Map successfully saved to {filename}")
    
