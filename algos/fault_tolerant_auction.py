from algos.market_auction import MarketAuction

class FaultTolerantAuctionManager:
    """
    Monitors active agent node failures and triggers immediate re-auctioning 
    of abandoned exploration frontiers to online swarm peers.
    """
    @staticmethod
    def handle_failed_agents(active_allocations, active_agents, failed_agent_ids, unassigned_frontiers):
        """
        Reclaims frontiers assigned to dead nodes and redistributes them 
        to active healthy swarm agents.
        """
        reclaimed_frontiers = list(unassigned_frontiers)
        
        # Strip tasks assigned to dead agents
        updated_allocations = {}
        for agent_id, target in active_allocations.items():
            if agent_id in failed_agent_ids:
                reclaimed_frontiers.append(target)
            else:
                updated_allocations[agent_id] = target
                
        # Re-run market auction for online agents with reclaimed tasks
        online_agents = [a for a in active_agents if a.agent_id not in failed_agent_ids]
        
        if online_agents and reclaimed_frontiers:
            new_allocations = MarketAuction.run_auction(online_agents, reclaimed_frontiers)
            updated_allocations.update(new_allocations)
            
        return updated_allocations
