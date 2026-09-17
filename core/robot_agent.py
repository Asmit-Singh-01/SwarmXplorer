import numpy as np
import random
from core.mesh_node import VirtualMeshNode
from algos.frontier_search import find_frontiers, get_best_frontier
from config import ROBOT_SPEED, SENSOR_RANGE, ARENA_WIDTH, ARENA_HEIGHT, GRID_SIZE, CELL_SIZE

class SwarmAgent:
    def __init__(self, agent_id, x, y):
        self.id = agent_id
        self.position = np.array([float(x), float(y)])
        self.heading = random.uniform(0, 2 * np.pi)
        self.mesh = VirtualMeshNode(agent_id)
        self.grid_map = np.zeros((GRID_SIZE, GRID_SIZE))

    def compute_repulsion(self, all_bot_positions):
        """Calculates collision avoidance forces with other bots."""
        force = np.array([0.0, 0.0])
        for bot_id, pos in all_bot_positions.items():
            if bot_id == self.id:
                continue
            dist = np.linalg.norm(self.position - pos)
            if 0 < dist < SENSOR_RANGE:
                force += (self.position - pos) / (dist ** 2)
        return force

    def update_occupancy_grid(self):
        """Marks current location as explored in local grid map."""
        grid_x = int(self.position[0] / CELL_SIZE)
        grid_y = int(self.position[1] / CELL_SIZE)
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
            self.grid_map[grid_x, grid_y] = 1.0

    def sync_map_with_neighbors(self, all_agents_dict):
        """Decentralized consensus: Merges maps with connected mesh neighbors."""
        for neighbor_id in self.mesh.neighbors:
            if neighbor_id in all_agents_dict:
                neighbor_map = all_agents_dict[neighbor_id].grid_map
                self.grid_map = np.maximum(self.grid_map, neighbor_map)

    def step(self, all_bot_positions, all_agents_dict):
        # 1. Update Mesh Network Connections
        self.mesh.update_connections(self.position, all_bot_positions)
        
        # 2. Frontier Exploration Brain Logic
        grid_x = int(self.position[0] / CELL_SIZE)
        grid_y = int(self.position[1] / CELL_SIZE)
        frontiers = find_frontiers(self.grid_map)
        target_frontier = get_best_frontier(np.array([grid_x, grid_y]), frontiers)

        if target_frontier is not None:
            target_pixel = target_frontier * CELL_SIZE
            frontier_dir = target_pixel - self.position
            norm_f = np.linalg.norm(frontier_dir)
            if norm_f > 0:
                frontier_dir = frontier_dir / norm_f
        else:
            frontier_dir = np.array([np.cos(self.heading), np.sin(self.heading)])

        # 3. Combine Collision Avoidance + Frontier Vector
        repulsion = self.compute_repulsion(all_bot_positions)
        desired_direction = frontier_dir + (repulsion * 15.0)
        
        norm = np.linalg.norm(desired_direction)
        if norm > 0:
            move_vector = (desired_direction / norm) * ROBOT_SPEED
            self.position += move_vector

        # 4. Arena Boundary Check
        if self.position[0] <= 10 or self.position[0] >= ARENA_WIDTH - 10:
            self.heading = np.pi - self.heading
        if self.position[1] <= 10 or self.position[1] >= ARENA_HEIGHT - 10:
            self.heading = -self.heading

        # 5. Local Mapping & Mesh Sync
        self.update_occupancy_grid()
        self.sync_map_with_neighbors(all_agents_dict)
        
