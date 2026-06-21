
 import heapq

def best_first_search(graph, start, goal, h):
    pq = [(h[start], start)]
    visited = set()

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            print("Goal Reached")
            return

        if current not in visited:
            print(current, end=" ")
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(pq, (h[neighbor], neighbor))

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

best_first_search(graph, 'A', 'G', h)
