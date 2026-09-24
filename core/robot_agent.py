import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, UNEXPLORED, FREE_SPACE

class RobotAgent:
    def __init__(self, agent_id, start_x, start_y):
        self.agent_id = agent_id
        self.position = np.array([start_x, start_y], dtype=int)
        
        # Har agent ka apna local map representation (2D Matrix)
        self.local_map = np.full((GRID_HEIGHT, GRID_WIDTH), UNEXPLORED, dtype=int)
        
        # Initial spawn spot ko explore mark karo
        self.update_map()

    def update_map(self):
        # Current position ko free space mark karo
        x, y = self.position
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.local_map[y, x] = FREE_SPACE

    def step(self):
        # Phase 1 simple movement: Rightward & Downward step (Boundary limit check ke saath)
        new_x = min(self.position[0] + 1, GRID_WIDTH - 1)
        new_y = min(self.position[1] + 1, GRID_HEIGHT - 1)
        
        self.position = np.array([new_x, new_y], dtype=int)
        self.update_map()
        
    def get_explored_percentage(self):
        # Kitna percentage map explore hua hai
        explored_cells = np.sum(self.local_map != UNEXPLORED)
        total_cells = GRID_WIDTH * GRID_HEIGHT
        return (explored_cells / total_cells) * 100
        
