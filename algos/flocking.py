import numpy as np

class FlockingController:
    @staticmethod
    def compute_flocking_vector(agent, all_agents, separation_dist=2.0):
        """
        Computes Reynolds-based flocking steering vectors (Separation, Cohesion).
        """
        pos_a = agent.position
        separation_force = np.zeros(2, dtype=float)
        cohesion_force = np.zeros(2, dtype=float)
        neighbor_count = 0

        for other in all_agents:
            if other.agent_id == agent.agent_id:
                continue

            pos_b = other.position
            dist = np.linalg.norm(pos_a - pos_b)

            if 0 < dist < separation_dist:
                # Separation: steer away from crowded neighbors
                repel = (pos_a - pos_b) / (dist ** 2)
                separation_force += repel
                neighbor_count += 1
                
            # Cohesion: pull towards neighbor positions
            cohesion_force += pos_b

        if neighbor_count > 0:
            cohesion_force = (cohesion_force / neighbor_count) - pos_a
            cohesion_force = cohesion_force / (np.linalg.norm(cohesion_force) + 1e-5)

        # Combined flocking steering correction vector
        steering = (separation_force * 1.5) + (cohesion_force * 0.5)
        return np.sign(steering).astype(int)
      
