import numpy as np
from config import UNEXPLORED, FREE_SPACE

def find_frontiers(grid_map):
    """
    Scans 2D grid matrix to find frontier cells (unexplored cells bordering explored free space).
    """
    frontiers = []
    rows, cols = grid_map.shape

    # Grid boundaries inside search
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid_map[r, c] == UNEXPLORED:
                # Agar cell unexplored hai aur iska koi neighbor FREE_SPACE hai, toh ye frontier hai
                neighbors = grid_map[r-1:r+2, c-1:c+2]
                if np.any(neighbors == FREE_SPACE):
                    frontiers.append((c, r))  # Stored as (x, y) coordinates

    return frontiers


def get_best_frontier(agent_pos, frontiers):
    """
    Calculates Euclidean distance to all detected frontiers and returns the closest one.
    """
    if not frontiers:
        return None

    agent_coords = np.array(agent_pos)
    distances = [np.linalg.norm(agent_coords - np.array(f)) for f in frontiers]
    closest_index = np.argmin(distances)
    
    return frontiers[closest_index]
    
