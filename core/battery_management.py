class BatteryManager:
    """
    Monitors robot battery discharge rates, motor power consumption, 
    and triggers automated Return-to-Base (RTB) low-power protocols.
    """
    def __init__(self, max_capacity_mah=5000.0, discharge_rate_per_step=25.0):
        self.max_capacity = max_capacity_mah
        self.current_charge = max_capacity_mah
        self.discharge_rate = discharge_rate_per_step
        self.is_rtb_triggered = False

    def consume_power(self, distance_moved, is_communicating=True):
        """Calculates energy drain based on physical motion and wireless transmission."""
        motion_cost = distance_moved * 2.0
        comm_cost = 5.0 if is_communicating else 1.0
        total_drain = self.discharge_rate + motion_cost + comm_cost
        
        self.current_charge = max(0.0, self.current_charge - total_drain)
        
        # Trigger RTB if battery drops below 20%
        if self.get_percentage() <= 20.0:
            self.is_rtb_triggered = True
            
        return self.current_charge

    def get_percentage(self):
        """Returns remaining battery life as a percentage."""
        return (self.current_charge / self.max_capacity) * 100.0

    def recharge(self):
        """Resets battery level to full capacity upon docking at the base station."""
        self.current_charge = self.max_capacity
        self.is_rtb_triggered = False
