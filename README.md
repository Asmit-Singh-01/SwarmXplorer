# 🤖 SwarmXplorer: Enterprise-Grade Decentralized Swarm Robotics Framework

<div align="center">

[![SwarmXplorer CI Pipeline](https://github.com/Asmit-Sim/SwarmXplorer/actions/workflows/simulation.yml/badge.svg)](https://github.com/Asmit-Sim/SwarmXplorer/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/status-production%20ready-success.svg)]()

*A high-performance, resilient, and fully modular decentralized multi-agent exploration and navigation engine designed from scratch.*

</div>

---

## 🚀 Overview

**SwarmXplorer** is an advanced simulation and control framework engineered for autonomous multi-robot systems. Built without heavy graphical frameworks or external simulation bloat, it focuses purely on **core algorithmic efficiency, distributed consensus, fault-tolerance, and hardware abstraction (ROS 2)**. 

The swarm operates in a completely decentralized topology—meaning there is no central server commanding the agents. Robots communicate via peer-to-peer (P2P) wireless mesh channels, build shared global maps, negotiate task distribution using economic auctions, and maintain rigid flocking formations while avoiding obstacles.

---

## 🏗️ System Architecture & Core Modules

```text
SwarmXplorer/
│
├── config.py                 # Global grid, LiDAR, and communication parameters
├── main.py                   # System orchestrator & simulation runner
│
├── core/
│   ├── environment.py        # 2D Ground truth occupancy grid & static walls
│   ├── robot_agent.py        # LiDAR ray-casting sensor model & state manager
│   ├── mesh_node.py          # P2P wireless proximity & map consensus (np.maximum)
│   ├── renderer.py           # Headless ASCII terminal 2D arena visualizer
│   ├── frontier_search.py    # Yamauchi decentralized frontier detection
│   ├── analytics.py          # Swarm distance, energy expenditure & coverage tracker
│   ├── fault_tolerance.py    # Heartbeat monitor & automatic dead-node isolation
│   └── hal_bridge.py         # Hardware Abstraction Layer for ROS2 telemetry (JSON/Topics)
│
├── algos/
│   ├── a_star_planner.py     # Optimal O(E log V) heuristic pathfinding engine
│   ├── flocking.py           # Reynolds' separation, alignment & cohesion controller
│   ├── leader_election.py    # Bully/ID-based decentralized coordinator election
│   └── market_auction.py     # Contract Net Protocol (CNP) / auction-based task allocation
│
└── tests/
    └── test_swarm.py         # Comprehensive automated pytest suite
