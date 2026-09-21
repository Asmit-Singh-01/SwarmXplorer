import numpy as np

def find_frontiers(grid_map):
    """
    Find unexplored frontier cells in the grid map.
    0: Unexplored, 1: Free, 2: Obstacle
    """
    frontiers = []
    rows, cols = grid_map.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid_map[r, c] == 1:  # Free space
                # Check adjacent cells for unexplored space (0)
                if np.any(grid_map[r-1:r+2, c-1:c+2] == 0):
                    frontiers.append((r, c))
    return frontiers

def get_best_frontier(robot_pos, frontiers):
    if not frontiers:
        return None
    # Pick closest frontier based on Euclidean distance
    distances = [np.linalg.norm(np.array(robot_pos) - np.array(f)) for f in frontiers]
    min_index = np.argmin(distances)
    return frontiers[min_index]
    
