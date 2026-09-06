# Practical Assignment 2: Problem Solving through Search

## College Campus Navigation using Search Algorithms

### 1. Aim

To implement and compare different Artificial Intelligence search algorithms based on path cost, nodes explored, and execution time.

### 2. Problem Statement

Find an efficient route from the **Main Gate to the Examination Hall** using different search techniques.

### 3. Algorithms Implemented

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Greedy Best-First Search
4. A* Search
5. Hill Climbing
6. N-Queens using Backtracking

### 4. Search Techniques

| Type | Algorithm |
|---|---|
| Uninformed | BFS, DFS |
| Informed | Greedy, A* |
| Local Search | Hill Climbing |
| CSP | N-Queens |

### 5. Optimal Route

**Main Gate → Cafeteria → Examination Block → Examination Hall**

**Total Cost = 220 m**

### 6. Performance Evaluation

The algorithms are compared using:

- Path found
- Total path cost
- Nodes explored
- Execution time

### 7. Technologies Used

- Python
- Jupyter Notebook / VS Code
- GitHub

### 8. Python Libraries

```python
import time
import heapq
from collections import deque
