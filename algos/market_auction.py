import numpy as np
from algos.a_star_planner import AStarPlanner

class MarketAuction:
    """
    Enhanced Contract Net Protocol (CNP) featuring Heterogeneous Capability Matching
    and exact A* path cost evaluation for multi-domain swarm tasks.
    """
    @staticmethod
    def run_auction(agents, frontiers, task_requirements=None):
        if not frontiers or not agents:
            return {}

        allocations = {}
        claimed_frontiers = set()

        sorted_agents = sorted(agents, key=lambda a: a.agent_id)

        for i, f in enumerate(frontiers):
            f_tuple = tuple(f)
            if f_tuple in claimed_frontiers:
                continue

            best_agent = None
            min_cost = float('inf')

            required_capability = task_requirements.get(i, "GENERAL") if task_requirements else "GENERAL"

            for agent in sorted_agents:
                agent_cap = getattr(agent, 'capability', 'GENERAL')
                if agent_cap != "GENERAL" and required_capability != "GENERAL" and agent_cap != required_capability:
                    continue

                # Compute path safely
                path = AStarPlanner.plan_path(agent.local_map, agent.position, f)
                cost = len(path) if path is not None else float('inf')

                if cost < min_cost:
                    min_cost = cost
                    best_agent = agent

            if best_agent is not None and best_agent.agent_id not in allocations.values():
                allocations[best_agent.agent_id] = f_tuple
                claimed_frontiers.add(f_tuple)

        return allocations
