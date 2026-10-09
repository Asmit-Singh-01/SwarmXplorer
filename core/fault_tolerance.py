import time

class SwarmHealthMonitor:
    def __init__(self, heartbeat_timeout=3.0):
        self.heartbeat_timeout = heartbeat_timeout
        self.last_seen = {}

    def register_agent(self, agent_id):
        self.last_seen[agent_id] = time.time()

    def update_heartbeat(self, agent_id):
        self.last_seen[agent_id] = time.time()

    def get_active_agents(self, agents):
        """
        Filters out unresponsive/failed agents from active swarm operations.
        """
        current_time = time.time()
        active = []
        for agent in agents:
            # Check if agent is alive
            if current_time - self.last_seen.get(agent.agent_id, 0) <= self.heartbeat_timeout:
                active.append(agent)
            else:
                print(f" [!] [HEALTH WARNING] Agent {agent.agent_id} unresponsive! Re-allocating tasks...")
        return active
      
