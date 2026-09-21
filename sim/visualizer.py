import matplotlib
matplotlib.use('Agg')  # Headless mode for CI/CD environments
import matplotlib.pyplot as plt

def save_swarm_map(bots, filename="swarm_exploration_map.png"):
    print("Simulation completed. Robot positions:")
    for bot in bots:
        pos = getattr(bot, 'position', [0, 0])
        bot_id = getattr(bot, 'id', 0)
        print(f"Agent {bot_id} at position {pos}")
        
