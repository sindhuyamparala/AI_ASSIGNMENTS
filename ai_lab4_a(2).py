import heapq

def a_star_search(graph, heuristic, start, goal):
    priority_queue = [(0 + heuristic[start], 0, start)]  
    visited = set()
    parent = {}
    g_cost = {start: 0}

    while priority_queue:
        _, cost, curr = heapq.heappop(priority_queue)

        if curr in visited:
            continue

        visited.add(curr)

        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = parent.get(curr)
            return path[::-1]

        for neighbor, move_cost in graph[curr].items():
            if neighbor in visited:
                continue

            new_g_cost = cost + move_cost  
            f_cost = new_g_cost + heuristic[neighbor]  

            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                heapq.heappush(priority_queue, (f_cost, new_g_cost, neighbor))
                parent[neighbor] = curr

    return None 

graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 2},
    'G': {}
}

heuristic = {
    'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0
}

start_node = 'S'
goal_node = 'G'
path = a_star_search(graph, heuristic, start_node, goal_node)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
