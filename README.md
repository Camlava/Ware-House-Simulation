# Warehouse Operations Simulation

## Project Status
This project implements a discrete-event simulation of warehouse operations
focused on order processing, inventory management, and robot routing.

### Implemented
- Core discrete-event simulation loop
- (Q, R) inventory management model
- Shortest-path robot routing using Dijkstra’s algorithm
- Entity classes for orders, robots, and inventory
- Initial performance metrics (order fulfillment time)

### In Progress
- Multi-robot coordination
- Congestion modeling
- Expanded data visualization

### Changes from Original Proposal
The simulation focuses exclusively on robotic automation and excludes
human labor variability to reduce model complexity.

---

## Installation Instructions

### Requirements
- Python 3.9+
- pip

### Setup
```bash
git clone https://github.com/yourusername/warehouse-simulation
cd warehouse-simulation
pip install -r requirements.txt