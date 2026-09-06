import time
import heapq
from collections import deque

# Campus graph
graph = {
    "Main Gate": {
        "Academic Block": 60,
        "Library": 80,
        "Cafeteria": 100
    },
    "Academic Block": {
        "Laboratory Block": 70
    },
    "Library": {
        "Administration Block": 50
    },
    "Cafeteria": {
        "Examination Block": 40
    },
    "Laboratory Block": {
        "Examination Hall": 250
    },
    "Administration Block": {
        "Examination Hall": 180
    },
    "Examination Block": {
        "Examination Hall": 80
    },
    "Examination Hall": {}
}

# Heuristic values
h = {
    "Main Gate": 220,
    "Academic Block": 320,
    "Library": 230,
    "Cafeteria": 120,
    "Laboratory Block": 250,
    "Administration Block": 180,
    "Examination Block": 80,
    "Examination Hall": 0
}

START = "Main Gate"
GOAL = "Examination Hall"


# BFS
def bfs(start, goal):

    queue = deque([(start, [start], 0)])
    visited = set()
    nodes = 0

    while queue:

        current, path, cost = queue.popleft()
        nodes += 1

        if current == goal:
            return path, cost, nodes

        if current in visited:
            continue

        visited.add(current)

        for location, distance in graph[current].items():

            if location not in visited:
                queue.append(
                    (location,
                     path + [location],
                     cost + distance)
                )

    return None, 0, nodes


# DFS
def dfs(start, goal):

    stack = [(start, [start], 0)]
    visited = set()
    nodes = 0

    while stack:

        current, path, cost = stack.pop()
        nodes += 1

        if current == goal:
            return path, cost, nodes

        if current in visited:
            continue

        visited.add(current)

        neighbours = list(graph[current].items())
        neighbours.reverse()

        for location, distance in neighbours:

            if location not in visited:
                stack.append(
                    (location,
                     path + [location],
                     cost + distance)
                )

    return None, 0, nodes


# Greedy Best-First Search
def greedy(start, goal):

    current = start
    path = [current]
    cost = 0
    visited = set()
    nodes = 0

    while current != goal:

        visited.add(current)
        nodes += 1

        candidates = [
            location
            for location in graph[current]
            if location not in visited
        ]

        if not candidates:
            return None, 0, nodes

        next_location = min(
            candidates,
            key=lambda location: h[location]
        )

        cost += graph[current][next_location]
        current = next_location
        path.append(current)

    nodes += 1

    return path, cost, nodes


# A* Search
def a_star(start, goal):

    priority_queue = [
        (h[start], 0, start, [start])
    ]

    best_cost = {start: 0}
    nodes = 0

    while priority_queue:

        f, g, current, path = heapq.heappop(
            priority_queue
        )

        nodes += 1

        if current == goal:
            return path, g, nodes

        for location, distance in graph[current].items():

            new_cost = g + distance

            if (
                location not in best_cost
                or new_cost < best_cost[location]
            ):

                best_cost[location] = new_cost

                new_f = new_cost + h[location]

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_cost,
                        location,
                        path + [location]
                    )
                )

    return None, 0, nodes


# Hill Climbing
def hill_climbing(start, goal):

    current = start
    path = [current]
    cost = 0
    nodes = 0

    while current != goal:

        nodes += 1

        neighbours = list(
            graph[current].items()
        )

        if not neighbours:
            return None, 0, nodes

        next_location, distance = min(
            neighbours,
            key=lambda item: h[item[0]]
        )

        if h[next_location] >= h[current]:
            return None, cost, nodes

        cost += distance
        current = next_location
        path.append(current)

    nodes += 1

    return path, cost, nodes


# N-Queens
def solve_n_queens(n):

    board = [-1] * n
    nodes = 0

    def is_safe(row, col):

        for previous_row in range(row):

            previous_col = board[previous_row]

            if previous_col == col:
                return False

            if abs(previous_col - col) == \
               abs(previous_row - row):
                return False

        return True

    def backtrack(row):

        nonlocal nodes
        nodes += 1

        if row == n:
            return True

        for col in range(n):

            if is_safe(row, col):

                board[row] = col

                if backtrack(row + 1):
                    return True

                board[row] = -1

        return False

    start_time = time.perf_counter()

    solved = backtrack(0)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return solved, board, nodes, execution_time


# Test algorithms
def test_algorithm(name, function):

    start_time = time.perf_counter()

    path, cost, nodes = function(
        START,
        GOAL
    )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print("\n" + "=" * 55)
    print("Algorithm:", name)
    print("=" * 55)

    if path:
        print("Path:", " -> ".join(path))
        print("Total Distance:", cost, "m")
    else:
        print("No solution found")

    print("Nodes Explored:", nodes)
    print(
        "Execution Time:",
        round(execution_time, 8),
        "seconds"
    )


# Main program
print("=" * 60)
print("COLLEGE CAMPUS SEARCH ALGORITHM EVALUATION")
print("=" * 60)

test_algorithm("Breadth First Search", bfs)
test_algorithm("Depth First Search", dfs)
test_algorithm("Greedy Best-First Search", greedy)
test_algorithm("A* Search", a_star)
test_algorithm("Hill Climbing", hill_climbing)


# N-Queens test
print("\n" + "=" * 60)
print("CONSTRAINT SATISFACTION - N QUEENS")
print("=" * 60)

n = 4

solved, board, nodes, execution_time = solve_n_queens(n)

if solved:
    print("N =", n)
    print("Solution:", board)
    print("Nodes Explored:", nodes)
    print(
        "Execution Time:",
        round(execution_time, 8),
        "seconds"
    )
else:
    print("No solution found")