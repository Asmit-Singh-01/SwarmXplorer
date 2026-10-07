import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, UNEXPLORED, FREE_SPACE, OBSTACLE

class Environment:
    def __init__(self):
        # Global Ground Truth Map
        self.grid = np.full((GRID_HEIGHT, GRID_WIDTH), FREE_SPACE, dtype=int)
        self.add_default_obstacles()

    def add_default_obstacles(self):
        """Generates static walls and obstacles in the arena."""
        # Perimeter Walls
        self.grid[0, :] = OBSTACLE
        self.grid[-1, :] = OBSTACLE
        self.grid[:, 0] = OBSTACLE
        self.grid[:, -1] = OBSTACLE

        # Internal Obstacle Blocks / Walls
        self.grid[5:15, 8] = OBSTACLE    # Vertical Wall
        self.grid[10, 12:18] = OBSTACLE  # Horizontal Wall
