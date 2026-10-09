import heapq
import numpy as np
from config import OBSTACLE, GRID_WIDTH, GRID_HEIGHT

class AStarPlanner:
    @staticmethod
    def heuristic(a, b):
        """Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @classmethod
    def plan_path(cls, grid, start, goal):
        """
        Computes optimal obstacle-free path from start to goal using A* algorithm.
        """
        start = tuple(start)
        goal = tuple(goal)
        
        if start == goal:
            return [start]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}
        f_score = {start: cls.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for dx, dy in neighbors:
                neighbor = (current[0] + dx, current[1] + dy)
                nx, ny = neighbor

                if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                    if grid[ny, nx] == OBSTACLE:
                        continue

                    tentative_g = g_score[current] + 1
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score[neighbor] = tentative_g + cls.heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return [start]  # Fallback if no path found
