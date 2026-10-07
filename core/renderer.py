import numpy as np
from config import UNEXPLORED, FREE_SPACE, OBSTACLE

class TerminalRenderer:
    @staticmethod
    def render(global_map, agents):
        """
        Renders a clean ASCII representation of the swarm environment.
        """
        height, width = global_map.shape
        # Visual Canvas setup
        canvas = np.full((height, width), '?', dtype=object)

        # Map Legends
        canvas[global_map == FREE_SPACE] = '.'
        canvas[global_map == OBSTACLE] = '#'
        canvas[global_map == UNEXPLORED] = '?'

        # Agent Overlay
        for agent in agents:
            x, y = agent.position
            if 0 <= x < width and 0 <= y < height:
                canvas[y, x] = f"A{agent.agent_id}"

        print("\n" + "=" * (width * 2 + 3))
        for row in canvas:
            print(" ".join(f"{val:>2}" for val in row))
        print("=" * (width * 2 + 3))
        print(" Legend: '.' Free | '#' Obstacle | '?' Unexplored | 'A0/A1' Agents\n")
      
