import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, UNEXPLORED, FREE_SPACE, OBSTACLE
from algos.a_star_planner import AStarPlanner
from algos.flocking import FlockingController

class RobotAgent:
    def __init__(self, agent_id, start_x, start_y, sensor_range=3):
        self.agent_id = agent_id
        self.position = np.array([start_x, start_y], dtype=int)
        self.sensor_range = sensor_range
        self.current_target = None
        self.total_distance_traveled = 0
        
        self.local_map = np.full((GRID_HEIGHT, GRID_WIDTH), UNEXPLORED, dtype=int)

    def scan_and_update_map(self, env_grid):
        cx, cy = self.position
        r = self.sensor_range

        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                target_x, target_y = cx + dx, cy + dy

                if 0 <= target_x < GRID_WIDTH and 0 <= target_y < GRID_HEIGHT:
                    steps = max(abs(dx), abs(dy))
                    if steps == 0:
                        self.local_map[cy, cx] = FREE_SPACE
                        continue

                    for step in range(1, steps + 1):
                        curr_x = int(round(cx + (dx * step / steps)))
                        curr_y = int(round(cy + (dy * step / steps)))

                        if 0 <= curr_x < GRID_WIDTH and 0 <= curr_y < GRID_HEIGHT:
                            cell_val = env_grid[curr_y, curr_x]
                            self.local_map[curr_y, curr_x] = cell_val
                            if cell_val == OBSTACLE:
                                break

    def step(self, env_grid, all_agents, assigned_target=None):
        self.scan_and_update_map(env_grid)

        if assigned_target is not None:
            self.current_target = tuple(assigned_target)
            path = AStarPlanner.plan_path(self.local_map, self.position, self.current_target)
            
            if len(path) > 1:
                next_spot = np.array(path[1])
                
                # Apply Flocking correction vector
                flock_vector = FlockingController.compute_flocking_vector(self, all_agents)
                adjusted_spot = next_spot + flock_vector
                
                ax, ay = np.clip(adjusted_spot, [0, 0], [GRID_WIDTH - 1, GRID_HEIGHT - 1])
                if self.local_map[ay, ax] != OBSTACLE:
                    next_spot = np.array([ax, ay])

                dx = abs(next_spot[0] - self.position[0])
                dy = abs(next_spot[1] - self.position[1])
                self.total_distance_traveled += (dx + dy)
                self.position = next_spot
        else:
            self.current_target = None

        self.scan_and_update_map(env_grid)
        return self.current_target

    def get_explored_percentage(self):
        explored_cells = np.sum(self.local_map != UNEXPLORED)
        total_cells = GRID_WIDTH * GRID_HEIGHT
        return (explored_cells / total_cells) * 100
        
