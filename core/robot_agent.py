import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, UNEXPLORED, FREE_SPACE, OBSTACLE
from core.frontier_search import find_frontiers, get_best_frontier

class RobotAgent:
    def __init__(self, agent_id, start_x, start_y, sensor_range=3):
        self.agent_id = agent_id
        self.position = np.array([start_x, start_y], dtype=int)
        self.sensor_range = sensor_range
        self.current_target = None
        
        self.local_map = np.full((GRID_HEIGHT, GRID_WIDTH), UNEXPLORED, dtype=int)

    def scan_and_update_map(self, env_grid):
        """
        Ray-Casting LiDAR simulation: Scans surroundings and stops vision at OBSTACLES.
        """
        cx, cy = self.position
        r = self.sensor_range

        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                target_x, target_y = cx + dx, cy + dy

                if 0 <= target_x < GRID_WIDTH and 0 <= target_y < GRID_HEIGHT:
                    # Bresenham/Simple line step check for obstacle blocking
                    steps = max(abs(dx), abs(dy))
                    if steps == 0:
                        self.local_map[cy, cx] = FREE_SPACE
                        continue

                    blocked = False
                    for step in range(1, steps + 1):
                        curr_x = int(round(cx + (dx * step / steps)))
                        curr_y = int(round(cy + (dy * step / steps)))

                        if 0 <= curr_x < GRID_WIDTH and 0 <= curr_y < GRID_HEIGHT:
                            cell_value = env_grid[curr_y, curr_x]
                            self.local_map[curr_y, curr_x] = cell_value
                            
                            if cell_value == OBSTACLE:
                                blocked = True
                                break  # Line of sight broken by obstacle!

    def step(self, env_grid, occupied_targets=None):
        # Update local map before deciding next move
        self.scan_and_update_map(env_grid)

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

            # Prevent stepping inside known obstacles
            if self.local_map[new_y, new_x] != OBSTACLE:
                self.position = np.array([new_x, new_y], dtype=int)
        else:
            self.current_target = None

        self.scan_and_update_map(env_grid)
        return self.current_target

    def get_explored_percentage(self):
        explored_cells = np.sum(self.local_map != UNEXPLORED)
        total_cells = GRID_WIDTH * GRID_HEIGHT
        return (explored_cells / total_cells) * 100
        
