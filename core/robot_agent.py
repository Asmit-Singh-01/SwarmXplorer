import sys
import os

# Root directory path insert for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algos.frontier_search import find_frontiers, get_best_frontier
from core.mesh_node import VirtualMeshNode
import config

class RobotAgent:
    def __init__(self, bot_id):
        self.id = bot_id
        self.position = [10.0 + bot_id * 5, 10.0 + bot_id * 5]
        self.mesh = VirtualMeshNode(bot_id)
        
    def step(self, all_bots):
        pass
        
