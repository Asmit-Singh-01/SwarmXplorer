# SwarmXplorer 🛸

*A Hardware-Agnostic, Decentralized Swarm Intelligence Framework for Autonomous Exploration & Spatial Mapping.*

---

## ⚡ Core Architecture

* **Decentralized Brain:** Yamauchi Frontier-Based Exploration for autonomous multi-agent targeting.
* **Virtual Mesh Network:** Range-limited P2P communication simulation with dynamic topology.
* **Occupancy Grid Consensus:** Real-time decentralized map merging across neighboring swarm nodes.
* **Hardware Abstraction Layer (HAL):** Simulation logic decoupled from hardware (ESP32 / ROS 2 ready).

---

## 📁 Repository Structure

```text
SwarmXplorer/
├── config.py         # Swarm physics & arena boundaries
├── core/
│   ├── mesh_node.py  # Peer-to-Peer network protocol
│   └── robot_agent.py# Agent controller & Frontier brain
├── algos/
│   └── frontier_search.py # Yamauchi frontier detection algorithm
├── sim/
│   └── visualizer.py # Matplotlib map generator
└── main.py           # Swarm simulation entrypoint
