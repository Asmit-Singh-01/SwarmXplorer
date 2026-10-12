from algos.leader_election import LeaderElection

def test_leader_election():
    agent_low = RobotAgent(agent_id=1, start_x=2, start_y=2)
    agent_high = RobotAgent(agent_id=5, start_x=5, start_y=5)
    
    active_agents = [agent_low, agent_high]
    leader = LeaderElection.elect_leader(active_agents)
    
    # Highest ID should be elected as leader
    assert leader.agent_id == 5
    
