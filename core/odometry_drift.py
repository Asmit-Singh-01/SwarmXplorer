import numpy as np

class OdometryDriftEstimator:
    """
    Simulates real-world mechanical wheel slippage, odometry drift, 
    and provides IMU-assisted bias compensation for ground rovers.
    """
    def __init__(self, drift_factor=0.05, slip_probability=0.1):
        self.drift_factor = drift_factor
        self.slip_probability = slip_probability

    def inject_drift_and_slip(self, true_velocity):
        """Simulates physical wheel slippage and noise on motor odometry."""
        vx, vy = true_velocity
        
        # Check for sudden wheel slip event
        slip_multiplier = 1.0
        if np.random.rand() < self.slip_probability:
            slip_multiplier = np.random.uniform(0.2, 0.6)  # Traction loss
            
        # Add systematic mechanical drift noise
        drift_x = np.random.normal(0, self.drift_factor)
        drift_y = np.random.normal(0, self.drift_factor)
        
        estimated_vx = (vx * slip_multiplier) + drift_x
        estimated_vy = (vy * slip_multiplier) + drift_y
        
        return np.array([estimated_vx, estimated_vy])

    @staticmethod
    def compensate_drift(estimated_pos, imu_yaw, step_distance):
        """Uses IMU heading data to correct cumulative odometry position error."""
        corrected_x = estimated_pos[0] + step_distance * np.cos(imu_yaw)
        corrected_y = estimated_pos[1] + step_distance * np.sin(imu_yaw)
        return np.array([corrected_x, corrected_y])
