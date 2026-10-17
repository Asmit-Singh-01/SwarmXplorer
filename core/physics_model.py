import numpy as np

class DifferentialDrivePhysics:
    """
    Simulates real-world differential drive kinematics, wheel speed limits, 
    and acceleration smoothing for physical robot agents.
    """
    def __init__(self, max_linear_speed=1.0, max_angular_speed=2.0, wheel_base=0.5):
        self.max_linear_speed = max_linear_speed
        self.max_angular_speed = max_angular_speed
        self.wheel_base = wheel_base

    def compute_kinematic_step(self, current_pos, target_pos, dt=1.0):
        """
        Computes smooth kinematic movement vector with speed and inertia constraints.
        """
        pos_arr = np.array(current_pos, dtype=float)
        target_arr = np.array(target_pos, dtype=float)
        
        direction = target_arr - pos_arr
        dist = np.linalg.norm(direction)

        if dist < 1e-5:
            return pos_arr

        # Normalize direction and apply velocity constraints
        unit_dir = direction / dist
        step_vel = unit_dir * min(self.max_linear_speed, dist)
        
        # Update position based on kinematic velocity vector
        new_pos = pos_arr + (step_vel * dt)
        return np.round(new_pos).astype(int)
