import heapq
import numpy as np

class MAPFEngine:
    """
    Multi-Agent Path Finding (MAPF) using Conflict-Based Search (CBS) 
    for collision-free space-time trajectory planning across the swarm.
    """
    @staticmethod
    def space_time_a_star(local_map, start, goal, constraints=None):
        """
        Computes an optimal path in Space-Time (x, y, time) avoiding space-time constraints.
        constraints: set of tuples (x, y, time) that are forbidden.
        """
        if constraints is None:
            constraints = set()

        start_node = (start[0], start[1], 0)
        goal_pos = tuple(goal)

        def heuristic(pos):
            return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])

        # Priority queue: (f_score, g_score, current_pos_time, path)
        open_set = []
        heapq.heappush(open_set, (heuristic(start), 0, start_node, [start_node]))
        
        g_scores = {start_node: 0}

        while open_set:
            f, g, current, path = heapq.heappop(open_set)
            cx, cy, ct = current

            if (cx, cy) == goal_pos:
                return path

            # Possible movements: 4-connected grid + wait action (staying in place)
            neighbors = [
                (cx + 1, cy, ct + 1),
                (cx - 1, cy, ct + 1),
                (cx, cy + 1, ct + 1),
                (cx, cy - 1, ct + 1),
                (cx, cy, ct + 1)  # Wait action
            ]

            for nx, ny, nt in neighbors:
                if 0 <= nx < local_map.shape[1] and 0 <= ny < local_map.shape[0]:
                    if local_map[ny, nx] == 2:  # Assuming 2 is obstacle
                        if (nx, ny) != goal_pos: # Allow reaching goal even if near obstacle
                            continue

                    next_state = (nx, ny, nt)
                    if next_state in constraints:
                        continue

                    tentative_g = g + 1

                    if next_state not in g_scores or tentative_g < g_scores[next_state]:
                        g_scores[next_state] = tentative_g
                        f_score = tentative_g + heuristic((nx, ny))
                        heapq.heappush(open_set, (f_score, tentative_g, next_state, path + [next_state]))

        return None # No conflict-free path found
