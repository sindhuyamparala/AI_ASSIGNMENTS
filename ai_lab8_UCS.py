

import heapq

graph = {
    'A': [('B', 10), ('C', 15)],
    'B': [('D', 12), ('F', 15)],
    'C': [('E', 10)],
    'D': [('E', 2), ('F', 1)],
    'F': [ ('E', 5)],
    'E': []
}

def uniform_cost_search(graph, start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for nbr, e_cost in graph.get(node, []):
            if nbr not in visited:
                new_cost = cost + e_cost
                new_path = path + [nbr]
                heapq.heappush(queue, (new_cost, new_path))

    return None, float('inf')  

path, total_cost = uniform_cost_search(graph, 'A', 'E')
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", total_cost)
