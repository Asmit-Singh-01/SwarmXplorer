import numpy as np

class VoxelGrid3D:
    """
    3D Volumetric Voxel Grid mapping engine for aerial drones and 3D terrain rovers,
    replacing traditional 2D occupancy grids with (X, Y, Z) spatial representation.
    """
    def __init__(self, width=20, height=20, depth=5, resolution=1.0):
        self.width = width
        self.height = height
        self.depth = depth
        self.resolution = resolution
        
        # 3D Matrix: 0 = Unexplored, 1 = Free, 2 = Obstacle/Solid
        self.voxel_map = np.zeros((depth, height, width), dtype=int)

    def update_voxel(self, x, y, z, state):
        """Updates a specific 3D coordinate state in the volumetric space."""
        if 0 <= x < self.width and 0 <= y < self.height and 0 <= z < self.depth:
            self.voxel_map[z, y, x] = state

    def get_local_volume(self, center_pos, radius=2):
        """Extracts a local 3D sub-volume around a robot's 3D coordinate."""
        cx, cy, cz = center_pos
        z_min = max(0, cz - radius)
        z_max = min(self.depth, cz + radius + 1)
        y_min = max(0, cy - radius)
        y_max = min(self.height, cy + radius + 1)
        x_min = max(0, cx - radius)
        x_max = min(self.width, cx + radius + 1)
        
        return self.voxel_map[z_min:z_max, y_min:y_max, x_min:x_max]
