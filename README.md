# SwarmXplorer 🛸

*A Hardware-Agnostic, Decentralized Swarm Intelligence Framework for Autonomous Exploration & Spatial Mapping.*

![Swarm Exploration Map](./swarm_exploration_map.png)

---

## ⚡ Core Architecture

* **Decentralized Brain:** Yamauchi Frontier-Based Exploration for autonomous multi-agent targeting.
* **Virtual Mesh Network:** Range-limited P2P communication simulation with dynamic topology.
* **Occupancy Grid Consensus:** Real-time decentralized map merging across neighboring swarm nodes.
* **Hardware Abstraction Layer (HAL):** Simulation logic decoupled from hardware (ESP32/ROS 2 ready).

---

```text
SwarmXplorer/
├── config.py             # Global simulation settings
├── core/
│   ├── mesh_node.py      # Simulated P2P Mesh Communication
│   └── robot_agent.py    # Independent Robot Brain + Sensors
├── sim/
│   └── visualizer.py     # Real-time Renderer
├── main.py               # Launcher
└── README.md
