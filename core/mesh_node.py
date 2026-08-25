import math

class VirtualMeshNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = []

    def update_connections(self, my_pos, all_nodes):
        """Simulates RF range limit. Connects only to nearby robots."""
        self.neighbors.clear()
        for other_id, other_pos in all_nodes.items():
            if other_id == self.node_id:
                continue
            dist = math.hypot(my_pos[0] - other_pos[0], my_pos[1] - other_pos[1])
            if dist <= 120:  # Match COMMUNICATION_RADIUS
                self.neighbors.append(other_id)

    def broadcast_packet(self, data):
        # Simulated mesh packet transmission
        return {"sender": self.node_id, "payload": data, "hops": self.neighbors}
          
