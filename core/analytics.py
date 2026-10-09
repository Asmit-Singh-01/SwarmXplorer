class SwarmAnalytics:
    @staticmethod
    def print_performance_report(agents, global_coverage):
        print("\n" + "=" * 60)
        print(" SWARM PERFORMANCE METRICS LOG")
        print("=" * 60)
        print(f" Total Global Arena Explored : {global_coverage:.2f}%")
        
        total_dist = 0
        for agent in agents:
            dist = agent.total_distance_traveled
            total_dist += dist
            print(f" -> Agent {agent.agent_id} Distance Traveled : {dist} units")
            
        print(f" Total Swarm Energy/Distance Expenditure : {total_dist} units")
        print("=" * 60 + "\n")
      
