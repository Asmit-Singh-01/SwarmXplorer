# SwarmXplorer 🛸

> **A Hardware-Agnostic, Decentralized Swarm Intelligence Framework for Autonomous Exploration & Spatial Mapping.*
[![Build Status](https://img.shields.io/badge/Status-In_Development-brightgreen)](#)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](#)

*A Hardware-Agnostic, Decentralized Swarm Intelligence Framework for Autonomous Exploration & Spatial Mapping.*

![Swarm Exploration Map](swarm_exploration_map.png)

## ⚡ Key Architecture

* **Decentralized Brain:** Yamauchi Frontier-Based Exploration for autonomous multi-agent targeting.
* **Virtual Mesh Network:** Range-limited P2P communication with zero single point of failure.
* **Occupancy Grid Consensus:** Real-time map merging across neighboring swarm agents.
* 
---

## ⚡ Key Architecture

* **Hardware Abstraction Layer (HAL):** Decouples simulation logic from real hardware (ESP32 / ROS2).
* **Virtual Mesh Network:** Range-limited P2P communication simulation with realistic packet drops.
* **Decentralized Brain:** Zero single point of failure; each node acts independently based on local consensus.

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
