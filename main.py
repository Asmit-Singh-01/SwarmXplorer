import time
from core.robot_agent import RobotAgent
from config import NUM_AGENTS, MAX_SIMULATION_STEPS

def main():
    print("=" * 50)
    print(" SwarmXplorer - Phase 1: Core Engine Initialized")
    print("=" * 50)

    # Initialize Swarm Agents at different starting coordinates
    agents = [
        RobotAgent(agent_id=0, start_x=0, start_y=0),
        RobotAgent(agent_id=1, start_x=5, start_y=5),
        RobotAgent(agent_id=2, start_x=10, start_y=10)
    ]

    print(f"[*] Spawned {NUM_AGENTS} Autonomous Agents in Grid.")

    # Execution Loop
    for step_num in range(1, MAX_SIMULATION_STEPS + 1):
        print(f"\n--- Simulation Step {step_num}/{MAX_SIMULATION_STEPS} ---")
        
        for agent in agents:
            agent.step()
            coverage = agent.get_explored_percentage()
            print(f"[Agent {agent.agent_id}] Pos: {agent.position.tolist()} | Local Exploration: {coverage:.2f}%")
        
        time.sleep(0.1)

    print("\n" + "=" * 50)
    print(" Simulation Run Completed Successfully.")
    print("=" * 50)

if __name__ == "__main__":
    main()
    
