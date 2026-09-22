import sys
import os

# Root directory path append karna taaki 'algos' folder mil sake
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from algos.frontier_search import find_frontiers, get_best_frontier

class RobotAgent:
    def __init__(self, agent_id, start_pos):
        self.agent_id = agent_id
        self.position = np.array(start_pos, dtype=float)
        self.local_map = np.zeros((50, 50), dtype=int)

    def step(self):
        frontiers = find_frontiers(self.local_map)
        target = get_best_frontier(self.position, frontiers)
        if target is not None:
            direction = np.array(target) - self.position
            norm = np.linalg.norm(direction)
            if norm > 0:
                self.position += (direction / norm)
        return self.position
        
