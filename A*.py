from queue import PriorityQueue

def a_star(start, goal, graph, h):
    pq = PriorityQueue()
    pq.put((h[start], 0, start))  # (f=g+h, g, node)

    visited = set()

    while not pq.empty():
        f, g, current = pq.get()

        if current == goal:
            print("Goal Reached")
            return

        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + h[neighbor]
                pq.put((f_new, g_new, neighbor))

# Graph with costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

a_star('A', 'G', graph, h)
