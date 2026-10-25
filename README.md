# 🤖 SwarmXplorer

<div align="center">

[![SwarmXplorer CI Pipeline](https://github.com/Asmit-Sim/SwarmXplorer/actions/workflows/simulation.yml/badge.svg)](https://github.com/Asmit-Sim/SwarmXplorer/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/status-production%20ready-success.svg)]()
[![Docker Ready](https://img.shields.io/badge/docker-containerized-blueviolet.svg)](Dockerfile)

*An enterprise-grade, decentralized heterogeneous multi-agent robotics framework designed for extreme, GPS-denied, and latency-heavy operational environments.*

</div>

---

## 🚀 Overview

**SwarmXplorer** is a high-performance simulation and control framework built from scratch for autonomous multi-robot swarms (Air, Land, Underground, and Underwater). Designed without heavy graphical bloat, it focuses purely on **core algorithmic efficiency, distributed P2P consensus, collision-free space-time trajectory planning, and robust fault-tolerance**.

In environments where centralized servers or continuous human intervention are impossible—such as planetary space exploration (Lunar/Martian caves), deep-sea trenches, or hazardous industrial disaster zones—SwarmXplorer enables autonomous agents to collaborate, negotiate tasks, and map unknown terrains seamlessly.

---

## 🏗️ System Architecture & Directory Structure

```text
SwarmXplorer/
│
├── config.yaml               # Centralized system and simulation configuration
├── config.py                 # Global parameter parser
├── main.py                   # System orchestrator & simulation loop
├── Dockerfile                # Containerization setup for cloud/edge deployment
├── docker-compose.yml        # Multi-node swarm mesh orchestration
│
├── core/
│   ├── robot_agent.py        # Core agent state manager & sensor ray-casting
│   ├── voxel_grid_3d.py      # 3D volumetric spatial mapping engine
│   ├── sensor_fusion.py      # Extended Kalman Filter (EKF) & Gaussian noise simulation
│   ├── behavior_states.py    # Autonomous operational state machine (Exploring, RTB, etc.)
│   └── telemetry_logger.py   # JSON blackbox mission recorder for post-flight audit
│
├── algos/
│   ├── a_star_planner.py     # Optimal O(E log V) heuristic pathfinding engine
│   ├── mapf_cbs.py           # Multi-Agent Path Finding via Conflict-Based Search (CBS)
│   ├── velocity_obstacles.py # Real-time dynamic collision avoidance (VO)
│   ├── frontier_detector.py  # Decentralized frontier-based exploration engine
│   ├── flocking.py           # Reynolds' separation, alignment & cohesion controller
│   └── market_auction.py     # Heterogeneous capability-aware Contract Net Protocol (CNP)
│
└── tests/
    └── test_swarm.py         # Comprehensive automated pytest test suite
