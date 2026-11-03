import numpy as np

class RelativeLocalizationEngine:
    """
    Simulates Ultra-Wideband (UWB) inter-agent ranging and relative localization 
    for GPS-denied multi-robot swarm positioning.
    """
    @staticmethod
    def compute_pairwise_distances(agent_positions):
        """Computes Euclidean distance matrix between all active swarm agents with UWB noise."""
        n = len(agent_positions)
        distances = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    pos_i = np.array(agent_positions[i])
                    pos_j = np.array(agent_positions[j])
                    true_dist = np.linalg.norm(pos_i - pos_j)
                    
                    # Inject realistic UWB sensor ranging noise (~2cm deviation)
                    noisy_dist = true_dist + np.random.normal(0, 0.02)
                    distances[i, j] = max(0.0, noisy_dist)
                    
        return distances
      
