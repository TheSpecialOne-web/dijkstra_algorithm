# Dijkstra Algorithm — Fuel-Constrained Shortest Path

A variant of Dijkstra's shortest path algorithm that models a vehicle driving between cities with **fuel constraints** and **gas stations**.

## Problem

Given:
- `N` cities and `M` roads forming a weighted graph
- A fuel tank with maximum capacity `L`
- A subset of cities marked as **gas stations** (refuel to full when visited)

Compute how many cities are reachable from city #1 without ever running out of fuel.

## Algorithm

Modified Dijkstra using a min-heap:

1. Initialize all distances to ∞, except the source = 0
2. Pop the city with the lowest fuel-used so far
3. If the city is a gas station → reset fuel-used to 0
4. For each neighbor, push if `(current_fuel_used + edge_weight) ≤ L`
5. Count how many cities have a final distance ≤ L

## Architecture

```
.
└── dijkstra_algorithm/
    ├── algorithm.py    # Main solver (input from stdin)
    └── input.txt       # Sample input
```

## Input format

```
N M L              # cities, roads, fuel capacity
0101...            # gas-station bitmap (length N)
u v d              # M lines: edge between u and v with weight d
...
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

No external dependencies (uses only `heapq` and `sys` from stdlib).

## Usage

```bash
python dijkstra_algorithm/algorithm.py < dijkstra_algorithm/input.txt
```

## Complexity

- Time: O((N + M) log N)
- Space: O(N + M)

## License

MIT
