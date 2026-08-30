import random
import numpy as np

from core.mesh_node import VirtualMeshNode
from config import ROBOT_SPEED

class SwarmAgent:
    def __init__(self, agent_id, x, y):
        self.id = agent_id
        self.position = np.array([float(x), float(y)])
        self.heading = random.uniform(0, 2 * np.pi)
        self.mesh = VirtualMeshNode(agent_id)
        self.local_map = {}  # Discovered map coordinates

    def step(self, all_bot_positions):
        # 1. Mesh connection update
        self.mesh.update_connections(self.position, all_bot_positions)
        
        # 2. Simple Random Walk with obstacle/border avoidance
        dx = np.cos(self.heading) * ROBOT_SPEED
        dy = np.sin(self.heading) * ROBOT_SPEED
        
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        # Arena Boundary check
        if 10 < new_x < 790 and 10 < new_y < 590:
            self.position += np.array([dx, dy])
        else:
            self.heading += np.pi  # Turn around
      
