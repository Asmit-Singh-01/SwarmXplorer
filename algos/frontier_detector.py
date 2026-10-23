import numpy as np
from config import FREE_SPACE, UNEXPLORED, OBSTACLE

class FrontierDetector:
    """
    Detects and extracts frontier clusters (boundaries between free space and unexplored space)
    to drive autonomous decentralized swarm exploration.
    """
    @staticmethod
    def extract_frontiers(local_map):
        frontiers = []
        height, width = local_map.shape

        for y in range(height):
            for x in range(width):
                if local_map[y, x] == FREE_SPACE:
                    # Check 4-connected neighbors for unexplored cells
                    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                    is_frontier = False
                    
                    for nx, ny in neighbors:
                        if 0 <= nx < width and 0 <= ny < height:
                            if local_map[ny, nx] == UNEXPLORED:
                                is_frontier = True
                                break
                    
                    if is_frontier:
                        frontiers.append([x, y])

        return frontiers
