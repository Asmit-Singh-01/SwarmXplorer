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


🧠 Core Technical Modules:
SwarmXplorer is structured into modular layers optimized for scalable swarm robotics execution:

 * Heterogeneous Capability Matching (algos/market_auction.py)
   * Implements an enhanced Contract Net Protocol (CNP) economic auction.
   * Filters bids based on robot domain capabilities (AIR, LAND, UNDERGROUND, UNDERWATER) ensuring specialized tasks are only assigned to qualified agents.

 * Space-Time Multi-Agent Path Finding (algos/mapf_cbs.py)
   * Combines Conflict-Based Search (CBS) with Space-Time A* path planning.
   * Plans trajectories accounting for both 2D spatial coordinates and time (t), preventing deadlocks and agent-on-agent collisions in confined tunnels or narrow corridors.

 * Dynamic Collision Avoidance (algos/velocity_obstacles.py)
   * Real-time Velocity Obstacles (VO) algorithm.
   * Adjusts agent velocity vectors dynamically to dodge unexpected moving obstacles or nearby agents safely mid-flight.

 * Sensor Fusion & EKF Estimation (core/sensor_fusion.py)
   * Simulates realistic Gaussian sensor noise on LiDAR readings and wheel odometry.
   * Processes raw data through Extended Kalman Filter (EKF) steps to output reliable state estimates.

 * 3D Volumetric Spatial Mapping (core/voxel_grid_3d.py)
   * Replaces traditional 2D occupancy grids with a 3D volumetric spatial voxel representation.
   * Crucial for aerial drones and subterranean rovers navigating multi-level subterranean or cave structures.

 * Blackbox Mission Auditing (core/telemetry_logger.py)
   * Records real-time simulation steps, agent positions, path trajectories, and global coverage percentages.
   * Exports structured JSON blackbox logs for post-mission analytics and safety auditing.


🛠️ Quick Start & Installation:

1. Local Setup
Clone the repository and install the required dependencies:
git clone [https://github.com/Asmit-Sim/SwarmXplorer.git](https://github.com/Asmit-Sim/SwarmXplorer.git)
cd SwarmXplorer.
pip install -r requirements.txt


2. Run the Simulation Engine
Execute the unified orchestration loop:
python main.py


3. Run Automated Tests
Validate the codebase using pytest:
pytest -v


4. Docker Containerization
Run the multi-node swarm setup locally using Docker Compose:
docker-compose up --build


💼 Open-Core Business Model:
SwarmXplorer follows an Open-Core Model designed for commercial scalability:

 * Open-Source Core (MIT License): The foundational simulation engine, pathfinding algorithms, frontier detection, and consensus models remain free for community research, students, and open-source developers.

 * Enterprise Add-ons (Proprietary / Paid): Advanced industrial modules—such as direct ROS 2 / PX4 hardware flight controller bridges, real-time cloud telemetry streaming dashboards, and multi-domain acoustic/RF mesh bridge drivers—are licensed separately for defense, space contractors, and enterprise automation clients.
📄 License.

This project is open-source under the MIT License.

---


