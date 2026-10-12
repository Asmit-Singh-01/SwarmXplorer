import numpy as np
from algos.a_star_planner import AStarPlanner

class MarketAuction:
    """
    Contract Net Protocol (CNP) / Auction-Based Task Allocation Engine.
    Agents bid on available frontiers based on exact A* motion planning path cost.
    """
    @staticmethod
    def run_auction(agents, frontiers):
        """
        Conducts a decentralized combinatorial auction where active agents 
        bid on available frontier tasks. Returns a dictionary mapping agent_id -> target.
        """
        if not frontiers or not agents:
            return {}

        allocations = {}
        claimed_frontiers = set()

        # Sort agents to ensure deterministic auction evaluation order
        sorted_agents = sorted(agents, key=lambda a: a.agent_id)

        for agent in sorted_agents:
            best_frontier = None
            min_cost = float('inf')

            for f in frontiers:
                f_tuple = tuple(f)
                if f_tuple in claimed_frontiers:
                    continue

                # Calculate actual movement cost using A* Pathfinder
                path = AStarPlanner.plan_path(agent.local_map, agent.position, f)
                cost = len(path) if path else float('inf')

                if cost < min_cost:
                    min_cost = cost
                    best_frontier = f_tuple

            if best_frontier is not None:
                allocations[agent.agent_id] = best_frontier
                claimed_frontiers.add(best_frontier)

        return allocations
      
