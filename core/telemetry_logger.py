import json
import os
from datetime import datetime

class SwarmTelemetryLogger:
    """
    Records and exports real-time swarm mission telemetry data into a structured 
    JSON blackbox log file for post-mission analytics and safety auditing.
    """
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file_path = os.path.join(self.log_dir, f"mission_telemetry_{timestamp}.json")
        self.session_logs = []

    def log_step(self, step_num, agents, global_coverage, leader_id):
        """Records telemetry snapshot for a specific simulation step."""
        step_data = {
            "step": step_num,
            "timestamp": datetime.now().isoformat(),
            "global_coverage_pct": round(global_coverage, 2),
            "leader_id": leader_id,
            "agents": [
                {
                    "agent_id": a.agent_id,
                    "position": a.position.tolist(),
                    "capability": getattr(a, 'capability', 'GENERAL'),
                    "distance_traveled": a.total_distance_traveled,
                    "current_target": list(a.current_target) if a.current_target else None
                }
                for a in agents
            ]
        }
        self.session_logs.append(step_data)

    def save_to_disk(self):
        """Flushes session telemetry logs to permanent JSON storage."""
        with open(self.log_file_path, 'w') as f:
            json.dump(self.session_logs, f, indent=4)
        return self.log_file_path
