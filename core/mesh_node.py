import numpy as np
from config import COMMUNICATION_RADIUS

class MeshNode:
    """
    Handles Peer-to-Peer dynamic network topology and spatial map consensus.
    """
    @staticmethod
    def is_in_range(pos_a, pos_b, comm_radius=COMMUNICATION_RADIUS):
        """Checks if two agents are within P2P wireless signal range."""
        dist = np.linalg.norm(np.array(pos_a) - np.array(pos_b))
        return dist <= comm_radius

    @staticmethod
    def sync_maps(agent_a, agent_b):
        """
        Executes bidirectional Occupancy Grid consensus merge between two agents.
        """
        merged_map = np.maximum(agent_a.local_map, agent_b.local_map)
        agent_a.local_map = merged_map.copy()
        agent_b.local_map = merged_map.copy()
        
