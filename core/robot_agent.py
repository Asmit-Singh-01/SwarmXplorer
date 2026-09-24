import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, UNEXPLORED, FREE_SPACE
from core.frontier_search import find_frontiers, get_best_frontier

class RobotAgent:
    def __init__(self, agent_id, start_x, start_y, sensor_range=3):
        self.agent_id = agent_id
        self.position = np.array([start_x, start_y], dtype=int)
        self.sensor_range = sensor_range
        self.current_target = None
        
        self.local_map = np.full((GRID_HEIGHT, GRID_WIDTH), UNEXPLORED, dtype=int)
        self.scan_and_update_map()

    def scan_and_update_map(self):
        cx, cy = self.position
        r = self.sensor_range

        x_min, x_max = max(0, cx - r), min(GRID_WIDTH, cx + r + 1)
        y_min, y_max = max(0, cy - r), min(GRID_HEIGHT, cy + r + 1)

        self.local_map[y_min:y_max, x_min:x_max] = FREE_SPACE

    def step(self, occupied_targets=None):
        frontiers = find_frontiers(self.local_map)
        target = get_best_frontier(self.position, frontiers, occupied_targets)
        
        if target is not None:
            self.current_target = tuple(target)
            target_x, target_y = target
            curr_x, curr_y = self.position

            dx = np.sign(target_x - curr_x)
            dy = np.sign(target_y - curr_y)

            new_x = np.clip(curr_x + dx, 0, GRID_WIDTH - 1)
            new_y = np.clip(curr_y + dy, 0, GRID_HEIGHT - 1)

            self.position = np.array([new_x, new_y], dtype=int)
        else:
            self.current_target = None

        self.scan_and_update_map()
        return self.current_target

    def get_explored_percentage(self):
        explored_cells = np.sum(self.local_map == FREE_SPACE)
        total_cells = GRID_WIDTH * GRID_HEIGHT
        return (explored_cells / total_cells) * 100
        
