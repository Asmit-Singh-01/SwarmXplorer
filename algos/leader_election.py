class LeaderElection:
    """
    Decentralized Leader Election consensus engine (Bully/ID-based variant).
    """
    @staticmethod
    def elect_leader(active_agents):
        """
        Elects a swarm coordinator node from the pool of active agents.
        Returns the Agent instance designated as the current leader.
        """
        if not active_agents:
            return None

        # Select the active agent with the highest agent_id as the cluster coordinator
        sorted_agents = sorted(active_agents, key=lambda a: a.agent_id, reverse=True)
        leader = sorted_agents[0]
        return leader
      
