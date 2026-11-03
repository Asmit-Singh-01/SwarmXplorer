import numpy as np

class ObstacleTrajectoryPredictor:
    """
    Predicts future positions of dynamic obstacles or moving agents 
    using linear velocity extrapolation and constant acceleration models.
    """
    def __init__(self, prediction_horizon_steps=5):
        self.horizon = prediction_horizon_steps

    def predict_trajectory(self, current_pos, current_velocity):
        """
        Extrapolates future trajectory coordinates over the given time horizon.
        """
        pos = np.array(current_pos, dtype=float)
        vel = np.array(current_velocity, dtype=float)
        
        trajectory = []
        for step in range(1, self.horizon + 1):
            future_pos = pos + (vel * step)
            trajectory.append(future_pos.tolist())
            
        return trajectory
      
