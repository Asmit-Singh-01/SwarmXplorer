import os

# Arena & Physics Configuration
ARENA_WIDTH = 100
ARENA_HEIGHT = 100
NUM_ROBOTS = 5
SIMULATION_STEPS = 50

# Communication & Sensor Limits
COMMUNICATION_RANGE = 25.0
COMMUNICATION_RADIUS = 25.0
SENSOR_RANGE = 15.0

# Matplotlib Non-Interactive Backend Fix for CI/CD
os.environ["MPLBACKEND"] = "Agg"
