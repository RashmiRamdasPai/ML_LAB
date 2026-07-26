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

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    heuristic[node] = int(input("Enter heuristic value: "))
    graph[node] = input("Enter neighbors separated by space: ").split()

start = input("Enter start node: ")
goal = input("Enter goal node: ")

best_first_search(start, goal, graph, heuristic)
