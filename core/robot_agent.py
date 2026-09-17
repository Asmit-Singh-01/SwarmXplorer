import numpy as np
import random
from core.mesh_node import VirtualMeshNode
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
            self.grid_map[grid_x, grid_y] = 1.0  # Explored cell

    def sync_map_with_neighbors(self, all_agents_dict):
        """Decentralized consensus: Merges maps with connected mesh neighbors."""
        for neighbor_id in self.mesh.neighbors:
            if neighbor_id in all_agents_dict:
                neighbor_map = all_agents_dict[neighbor_id].grid_map
                # Bitwise OR operation to merge discovered cells
                self.grid_map = np.maximum(self.grid_map, neighbor_map)

    def step(self, all_bot_positions, all_agents_dict):
        # 1. Update Mesh Network Connections
        self.mesh.update_connections(self.position, all_bot_positions)
        
        # 2. Physics & Collision Avoidance Logic
        repulsion = self.compute_repulsion(all_bot_positions)
        forward_vector = np.array([np.cos(self.heading), np.sin(self.heading)])
        desired_direction = forward_vector + (repulsion * 10.0)
        
        # Normalize and Move
        norm = np.linalg.norm(desired_direction)
        if norm > 0:
            move_vector = (desired_direction / norm) * ROBOT_SPEED
            self.position += move_vector

        # 3. Arena Boundary Bouncing
        if self.position[0] <= 10 or self.position[0] >= ARENA_WIDTH - 10:
            self.heading = np.pi - self.heading
        if self.position[1] <= 10 or self.position[1] >= ARENA_HEIGHT - 10:
            self.heading = -self.heading

        # 4. Local Mapping & Peer Syncing
        self.update_occupancy_grid()
        self.sync_map_with_neighbors(all_agents_dict)
        
