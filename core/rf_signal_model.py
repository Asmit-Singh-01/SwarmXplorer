import numpy as np

class RFSignalPropagationModel:
    """
    Simulates real-world LoRa/ESP-NOW radio frequency attenuation, 
    path loss over distance, and wall obstacle interference for P2P mesh links.
    """
    def __init__(self, tx_power_dbm=20.0, frequency_mhz=915.0):
        self.tx_power_dbm = tx_power_dbm
        self.frequency_mhz = frequency_mhz

    def calculate_rssi(self, distance_meters, wall_count=0):
        """
        Computes Received Signal Strength Indicator (RSSI) using the 
        Log-Distance Path Loss Model with obstacle attenuation.
        """
        if distance_meters <= 0:
            return self.tx_power_dbm

        # Free space path loss exponent (n ~ 2.0 to 3.5 in structured environments)
        n = 2.7 
        path_loss_intercept = 20 * np.log10(self.frequency_mhz) - 27.55
        
        path_loss = path_loss_intercept + (10 * n * np.log10(distance_meters))
        
        # Add attenuation per wall obstruction (approx 12 dBm loss per concrete wall)
        wall_attenuation = wall_count * 12.0
        
        rssi = self.tx_power_dbm - (path_loss + wall_attenuation)
        return float(rssi)

    def estimate_packet_delivery_ratio(self, rssi):
        """Estimates Packet Delivery Ratio (PDR) reliability percentage based on RSSI threshold."""
        # Sensitivity threshold typically around -120 dBm for LoRa
        if rssi >= -90:
            return 1.0  # 100% delivery
        elif rssi <= -120:
            return 0.0  # Complete link drop
        else:
            # Linear transition degradation
            return float((rssi - (-120)) / (-90 - (-120)))
