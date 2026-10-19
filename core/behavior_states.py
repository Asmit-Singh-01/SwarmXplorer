from enum import Enum
import numpy as np

class RobotState(Enum):
    EXPLORING = 1
    RETURNING_BASE = 2
    REGROUPING = 3
    FAULT_RECOVERY = 4

class BehaviorStateMachine:
    """
    Manages autonomous operational state transitions for individual swarm agents 
    based on battery levels, distance traveled, and mesh connectivity.
    """
    @staticmethod
    def evaluate_state(agent, max_energy_distance=100, base_station_pos=(0, 0)):
        # Check if energy/distance budget is running low -> Return to Base
        if getattr(agent, 'total_distance_traveled', 0) >= max_energy_distance:
            return RobotState.RETURNING_BASE

        # Default state
        return RobotState.EXPLORING

    @staticmethod
    def execute_behavior(agent, base_station_pos=(0, 0)):
        current_state = BehaviorStateMachine.evaluate_state(agent)
        
        if current_state == RobotState.RETURNING_BASE:
            # Override target to move back to base station
            return np.array(base_station_pos, dtype=int), current_state
            
        return None, current_state
