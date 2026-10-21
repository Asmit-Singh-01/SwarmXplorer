import numpy as np

class VelocityObstacles:
    """
    Computes Velocity Obstacles (VO) for real-time dynamic collision avoidance 
    between moving swarm agents and unexpected obstacles.
    """
    @staticmethod
    def compute_safe_velocity(current_pos, preferred_velocity, neighbor_positions, neighbor_velocities, robot_radius=0.8, time_horizon=2.0):
        """
        Adjusts preferred velocity vector to avoid potential collisions with nearby agents.
        """
        adjusted_velocity = np.array(preferred_velocity, dtype=float)
        pos_a = np.array(current_pos, dtype=float)

        for p_b, v_b in zip(neighbor_positions, neighbor_velocities):
            pos_b = np.array(p_b, dtype=float)
            vel_b = np.array(v_b, dtype=float)
            
            relative_pos = pos_b - pos_a
            relative_vel = adjusted_velocity - vel_b
            
            dist = np.linalg.norm(relative_pos)
            combined_radius = robot_radius * 2.0

            if dist < combined_radius * 1.5:
                # Emergency repulsion vector away from close neighbor
                repulsion = pos_a - pos_b
                norm_rep = np.linalg.norm(repulsion)
                if norm_rep > 0:
                    adjusted_velocity += (repulsion / norm_rep) * 1.5

        return adjusted_velocity
