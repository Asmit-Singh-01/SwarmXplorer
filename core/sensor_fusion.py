import numpy as np

class SensorNoiseFilter:
    """
    Simulates real-world sensor noise (Gaussian noise on LiDAR & Odometry)
    and applies an Extended Kalman Filter (EKF) estimation loop.
    """
    @staticmethod
    def add_lidar_noise(true_distance, noise_level=0.15):
        """Injects real-world Gaussian sensor noise into distance measurements."""
        noise = np.random.normal(0, noise_level)
        return max(0.0, true_distance + noise)

    @staticmethod
    def kalman_filter_step(estimated_state, measurement, covariance, process_variance=0.01, measurement_variance=0.1):
        """
        Simplified 1D/2D EKF prediction and update step for smoothing noisy robot telemetry.
        """
        # Prediction step
        predicted_state = estimated_state
        predicted_cov = covariance + process_variance

        # Update step (Kalman Gain calculation)
        kalman_gain = predicted_cov / (predicted_cov + measurement_variance)
        updated_state = predicted_state + kalman_gain * (measurement - predicted_state)
        updated_cov = (1 - kalman_gain) * predicted_cov

        return updated_state, updated_cov
