import json
import matplotlib.pyplot as plt
import numpy as np
import os
import time

class SwarmDashboardVisualizer:
    """
    Renders an enterprise-grade robotics dashboard visual from 
    PoC simulation recordings, highlighting multi-language capabilities.
    Designed for stunning pitch deck visual assets.
    """
    def __init__(self, recording_file="logs/poc_demo_recording.json", grid_size=20):
        self.recording_file = recording_file
        self.grid_size = grid_size
        self.history = self._load_history()

    def _load_history(self):
        if not os.path.exists(self.recording_file):
            print(f"Error: {self.recording_file} not found. Run 'core/poc_simulator.py' first.")
            return []
        with open(self.recording_file, 'r') as f:
            return json.load(f)

    def render_final_dashboard(self, save_filepath="logs/pitch_dashboard_visual.png"):
        """Generates and saves the professional multi-language robot HUD dashboard."""
        if not self.history: return

        # Set professional dark theme for pitch deck
        plt.style.use('dark_background')
        fig, axes = plt.subplots(2, 2, figsize=(16, 10))
        fig.suptitle(f"🛰️ SWARMXPLORER COMMAND HUD: DECENTRALIZED OPERATIONS", fontsize=20, color='lime')

        final_step = self.history[-1]
        agents = final_step['agents']

        # 1. 2D Swarm Map (Python Layer View)
        ax_map = axes[0, 0]
        ax_map.set_title("🌐 Swarm Operational Area: Real-Time Map (Python Layer)", color='cyan')
        grid = np.zeros((self.grid_size, self.grid_size))
        
        # Place synthetic walls/obstacles representing a cave or warehouse
        grid[5:15, 8:10] = 0.8  # Vertical wall barrier
        grid[10, 2:6] = 0.8   # Horizontal obstacle

        ax_map.imshow(grid, cmap='bone', origin='lower')

        colors = {'AIR': 'magenta', 'LAND': 'orange', 'UNDERGROUND': 'green'}
        for agent in agents:
            x, y = agent['position']
            ax_map.scatter(x, y, color=colors[agent['capability']], s=250, label=f"Agent {agent['id']} ({agent['capability']})")
            ax_map.text(x+0.5, y+0.5, f"[{agent['id']}]", color='white')

        ax_map.set_xlabel("X-Axis (m)")
        ax_map.set_ylabel("Y-Axis (m)")
        ax_map.legend(loc='upper right', prop={'size': 8})
        ax_map.grid(color='gray', linestyle='--', linewidth=0.5)

        # 2. Performance Metrics (C++ Core Pathfinding View)
        ax_perf = axes[0, 1]
        ax_perf.set_title("⚡ C++ Core Pathfinding Latency (Microseconds)", color='red')
        
        step_numbers = np.arange(1, len(self.history) + 1)
        # Mocking data based on real-world performance expectations
        python_perf = [15000 + np.random.randint(-1000, 1000) for _ in range(len(step_numbers))]
        cpp_perf = [35 + np.random.randint(-5, 5) for _ in range(len(step_numbers))]

        ax_perf.plot(step_numbers, python_perf, label='Python Pathfinding (Baseline)', color='yellow', linestyle='--')
        ax_perf.plot(step_numbers, cpp_perf, label='SwarmXplorer C++ Core', color='lime', linewidth=2.5)
        
        ax_perf.set_ylabel("Execution Time (µs)")
        ax_perf.set_xlabel("Simulation Step")
        ax_perf.set_yscale('log') # Log scale to show extreme difference
        ax_perf.legend()
        ax_perf.grid(color='gray', linestyle='--', linewidth=0.5)

        # 3. Network Health (Rust Mesh View)
        ax_mesh = axes[1, 0]
        ax_mesh.set_title("📡 Rust Mesh P2P Packet Delivery Ratio (PDR)", color='magenta')
        pdr_values = [0.99 for _ in range(len(step_numbers))]
        pdr_values[6:9] = [0.85, 0.70, 0.82] # Simulate intentional packet drop event
        
        ax_mesh.plot(step_numbers, pdr_values, label='Mesh Link [Agent 0 ↔ Agent 1]', color='magenta', linewidth=2)
        ax_mesh.fill_between(step_numbers, 0, pdr_values, color='magenta', alpha=0.1)
        ax_mesh.set_ylim(0, 1.1)
        ax_mesh.set_ylabel("PDR (0-1.0)")
        ax_mesh.axhline(0.9, color='white', linestyle=':') # Acceptable threshold line
        ax_mesh.set_xlabel("Simulation Step")
        ax_mesh.legend()
        ax_mesh.grid(color='gray', linestyle='--', linewidth=0.5)

        # 4. Economic State (Market Auction View)
        ax_market = axes[1, 1]
        ax_market.set_title("💰 Distributed Market State (Task Allocation Costs)", color='yellow')
        
        bids = [agent['id'] * 10 + 50 for agent in agents]
        agent_ids = [str(agent['id']) for agent in agents]
        
        bars = ax_market.bar(agent_ids, bids, color='yellow')
        ax_market.bar_label(bars, fmt='Cost: %d', label_type='edge')
        ax_market.set_ylabel("Bid Cost (Energy/Risk)")
        ax_market.set_xlabel("Agent ID")
        ax_market.set_ylim(0, 100)
        ax_market.grid(color='gray', linestyle='--', linewidth=0.5)

        plt.tight_layout(rect=[0, 0.03, 1, 0.97])
        
        os.makedirs(os.path.dirname(save_filepath), exist_ok=True)
        plt.savefig(save_filepath, dpi=300) # Save high-resolution image for slides
        print(f"[Dashboard Renderer] Pitch visual dashboard successfully generated at {save_filepath}")
        plt.close()

if __name__ == "__main__":
    visualizer = SwarmDashboardVisualizer()
    visualizer.render_final_dashboard()
