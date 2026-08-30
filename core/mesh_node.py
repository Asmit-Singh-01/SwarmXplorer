import math
from config import COMMUNICATION_RADIUS


class VirtualMeshNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = []

    def update_connections(self, my_pos, all_nodes):
        """Connect to robots within the configured communication radius."""
        self.neighbors.clear()

        for other_id, other_pos in all_nodes.items():
            if other_id == self.node_id:
                continue

            distance = math.hypot(
                my_pos[0] - other_pos[0],
                my_pos[1] - other_pos[1]
            )

            if distance <= COMMUNICATION_RADIUS:
                self.neighbors.append(other_id)

    def broadcast_packet(self, data):
        """Create a simulated packet for future mesh communication."""
        return {
            "sender": self.node_id,
            "payload": data,
            "hops": self.neighbors.copy()
        }
