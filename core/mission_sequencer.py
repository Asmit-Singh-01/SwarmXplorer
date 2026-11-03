class MissionSequencer:
    """
    Manages high-level mission lifecycle states, phase transitions, 
    and safety triggers for autonomous swarm agents during field execution.
    """
    STATES = ["INIT", "DEPLOYING", "EXPLORING", "RETURNING_TO_BASE", "COMPLETED"]

    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.current_state = "INIT"
        self.milestones_reached = 0

    def update_state(self, battery_pct, coverage_pct, target_reached=False):
        """Evaluates operational metrics and executes safe state transitions."""
        # Critical safety override: Low battery forces RTB immediately
        if battery_pct <= 20.0:
            self.current_state = "RETURNING_TO_BASE"
            return self.current_state

        if self.current_state == "INIT":
            self.current_state = "DEPLOYING"
        elif self.current_state == "DEPLOYING" and target_reached:
            self.current_state = "EXPLORING"
        elif self.current_state == "EXPLORING" and coverage_pct >= 95.0:
            self.current_state = "COMPLETED"

        return self.current_state

    def get_status(self):
        """Returns current mission telemetry state summary."""
        return {
            "agent_id": self.agent_id,
            "state": self.current_state,
            "milestones": self.milestones_reached
        }
      
