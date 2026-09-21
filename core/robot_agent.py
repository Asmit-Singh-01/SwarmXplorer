import numpy as np
from algos.frontier_search import find_frontiers, get_best_frontier

class RobotAgent:
    def __init__(self, agent_id, start_pos):
        self.agent_id = agent_id
        self.position = np.array(start_pos, dtype=float)
        self.local_map = np.zeros((50, 50), dtype=int)

    def step(self):
        # Basic movement logic towards unexplored area
        frontiers = find_frontiers(self.local_map)
        target = get_best_frontier(self.position, frontiers)
        if target is not None:
            direction = np.array(target) - self.position
            norm = np.linalg.norm(direction)
            if norm > 0:
                self.position += (direction / norm)
        return self.position
        
