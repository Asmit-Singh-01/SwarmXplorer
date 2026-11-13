import numpy as np
import os
import json

class PoCSimulationEngine:
    """
    Executes a controlled multi-agent swarm mission and records 
    frame-by-frame spatial logs for PoC video generation and auditing.
    """
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.frames_history = []

        def setup_obstacle_course(self):
        # Safe obstacle placement bounded within grid dimensions
        h, w = self.grid.shape
        if h > 10 and w > 10:
            self.grid[5:min(15, h), min(8, w-1):min(10, w)] = 1  
            self.grid[min(10, h-1), min(2, w-1):min(6, w)] = 1   
        else:
            # For smaller test grids, place safe internal obstacles
            self.grid[min(2, h-1), min(2, w-1)] = 1


    def run_simulation_steps(self, steps=15):
        self.setup_obstacle_course()
        
        # Initialize heterogeneous agents [id, x, y, capability]
        agents = [
            {"id": 0, "pos": [2, 2], "cap": "AIR", "path": [[2,2]]},
            {"id": 1, "pos": [2, 18], "cap": "LAND", "path": [[2,18]]},
            {"id": 2, "pos": [18, 2], "cap": "UNDERGROUND", "path": [[18,2]]}
        ]

        for step in range(steps):
            frame_data = {"step": step, "agents": []}
            
            for agent in agents:
                # Simulate simple movement towards center exploring frontiers
                x, y = agent["pos"]
                if step < 8:
                    x += 1
                else:
                    y += 1
                
                # Boundary clamping
                x = max(0, min(x, self.width - 1))
                y = max(0, min(y, self.height - 1))
                agent["pos"] = [x, y]
                agent["path"].append([x, y])
                
                frame_data["agents"].append({
                    "id": agent["id"],
                    "capability": agent["cap"],
                    "position": [x, y]
                })
            
            self.frames_history.append(frame_data)
        
        return self.frames_history

    def export_poc_recording(self, filepath="logs/poc_demo_recording.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        history = self.run_simulation_steps()
        with open(filepath, "w") as f:
            json.dump(history, f, indent=4)
        print(f"[PoC Engine] Simulation recording successfully exported to {filepath}")

if __name__ == "__main__":
    sim = PoCSimulationEngine()
    sim.export_poc_recording()
  
