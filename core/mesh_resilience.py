import time

class MeshResilienceHandler:
    """
    Handles real-world wireless mesh packet loss, link timeouts, 
    and heartbeat dropouts for decentralized swarm agents.
    """
    def __init__(self, agent_id, heartbeat_timeout_sec=3.0):
        self.agent_id = agent_id
        self.heartbeat_timeout = heartbeat_timeout_sec
        self.last_seen_timestamps = {}
        self.connection_status = {}

    def update_heartbeat(self, neighbor_id):
        """Records a successful packet reception from a peer agent."""
        self.last_seen_timestamps[neighbor_id] = time.time()
        self.connection_status[neighbor_id] = True

    def check_link_health(self):
        """Evaluates if any peer link has timed out due to packet loss."""
        current_time = time.time()
        disconnected_nodes = []

        for neighbor_id, last_time in self.last_seen_timestamps.items():
            if current_time - last_time > self.heartbeat_timeout:
                self.connection_status[neighbor_id] = False
                disconnected_nodes.append(neighbor_id)

        return disconnected_nodes
