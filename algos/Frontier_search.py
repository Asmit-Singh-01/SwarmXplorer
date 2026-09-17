import numpy as np
from config import GRID_SIZE

def find_frontiers(grid_map):
    """
    Finds frontier cells (explored cells adjacent to unexplored territory).
    0 = Unexplored, 1 = Explored
    """
    frontiers = []
    
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            # If current cell is explored
            if grid_map[x, y] == 1.0:
                # Check neighbors (4-connectivity)
                neighbors = [
                    grid_map[x + 1, y],
                    grid_map[x - 1, y],
                    grid_map[x, y + 1],
                    grid_map[x, y - 1]
                ]
                # If any neighbor is unexplored (0.0), it's a frontier edge!
                if 0.0 in neighbors:
                    frontiers.append((x, y))
                    
    return frontiers

def get_best_frontier(agent_pos_grid, frontiers):
    """Selects the nearest frontier target for the robot."""
    if not frontiers:
        return None
    
    frontiers_arr = np.array(frontiers)
    distances = np.linalg.norm(frontiers_arr - agent_pos_grid, axis=1)
    nearest_idx = np.argmin(distances)
    
    return frontiers_arr[nearest_idx]

