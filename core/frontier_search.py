import numpy as np
from config import UNEXPLORED, FREE_SPACE

def find_frontiers(grid_map):
    frontiers = []
    rows, cols = grid_map.shape

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid_map[r, c] == UNEXPLORED:
                neighbors = grid_map[r-1:r+2, c-1:c+2]
                if np.any(neighbors == FREE_SPACE):
                    frontiers.append((c, r))

    return frontiers

def get_best_frontier(agent_pos, frontiers, occupied_targets=None):
    """
    Finds the closest frontier target that is NOT already claimed by another agent.
    """
    if not frontiers:
        return None

    if occupied_targets is None:
        occupied_targets = []

    # Exclude targets that other agents are already heading towards
    available_frontiers = [f for f in frontiers if tuple(f) not in occupied_targets]

    if not available_frontiers:
        # Fallback to any remaining frontier if all are claimed
        available_frontiers = frontiers

    agent_coords = np.array(agent_pos)
    distances = [np.linalg.norm(agent_coords - np.array(f)) for f in available_frontiers]
    closest_index = np.argmin(distances)
    
    return available_frontiers[closest_index]
    
