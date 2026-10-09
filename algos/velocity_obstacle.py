import numpy as np

class VelocityObstacle:
    @staticmethod
    def compute_safe_velocity(agent, other_agents, desired_velocity, safety_radius=1.5):
        """
        Adjusts agent velocity vector to prevent collision with nearby moving agents.
        """
        pos_a = agent.position
        vel_a = np.array(desired_velocity)

        for other in other_agents:
            if other.agent_id == agent.agent_id:
                continue

            pos_b = other.position
            dist = np.linalg.norm(pos_a - pos_b)

            # If within safety radius, project repellent vector
            if dist < safety_radius and dist > 0:
                repellent = (pos_a - pos_b) / dist
                vel_a = vel_a + repellent

        return np.sign(vel_a).astype(int)
      
