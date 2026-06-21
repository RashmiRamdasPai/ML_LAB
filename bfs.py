from queue import PriorityQueue

def best_first_search(start, goal, graph, h):
    visited = set()
    pq = PriorityQueue()

    pq.put((h[start], start))

    while not pq.empty():
        heuristic, current = pq.get()

        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        if current == goal:
            print("\nGoal Reached!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((h[neighbor], neighbor))

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

best_first_search('A', 'G', graph, h)
