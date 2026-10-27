import os
import time
import numpy as np

class LiveVisualizer:
    """
    Renders a high-tech sci-fi command center HUD for swarm live execution.
    Designed for generating stunning demo recordings and GIFs for cold emails.
    """
    @staticmethod
    def render_frame(step, agents, grid, coverage):
        # Clear terminal screen for smooth frame-by-frame animation
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("╔══════════════════════════════════════════════════════╗")
        print(f"║ 🤖 SWARMXPLORER LIVE COMMAND HUD   [STEP: {step:03d}]       ║")
        print(f"║ 📊 Global Coverage: {coverage:05.2f}%       | Active Swarm: {len(agents)} ║")
        print("╚══════════════════════════════════════════════════════╝")
        
        h, w = grid.shape
        display_grid = grid.copy()
        
        # Place agents on preview grid
        for agent in agents:
            ax, ay = int(agent.position[0]), int(agent.position[1])
            if 0 <= ax < w and 0 <= ay < h:
                display_grid[ay, ax] = 99  # Agent marker ID
                
        # Render map window (clipped to 15x25 for clean terminal fit)
        print("  Terrain Map & Agent Telemetry:")
        for y in range(min(h, 15)):
            row_str = "  "
            for x in range(min(w, 20)):
                val = display_grid[y, x]
                if val == 99:
                    row_str += "🛸"  # Drone / Agent
                elif val > 0:
                    row_str += "🧱"  # Obstacle / Wall
                else:
                    row_str += "⬛"  # Unexplored / Free space
            print(row_str)
            
        print("------------------------------------------------------")
        print(" Active Agent Status Telemetry:")
        for agent in agents:
            cap = getattr(agent, 'capability', 'GEN')
            pos = agent.position
            dist = agent.total_distance_traveled
            print(f"  > Agent [{agent.agent_id}] ({cap}) -> Pos:({pos[0]:02d},{pos[1]:02d}) | Dist: {dist:03d}m")
        print("======================================================")
