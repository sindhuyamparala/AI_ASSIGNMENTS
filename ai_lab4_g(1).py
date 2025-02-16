import heapq

def greedy_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]  
    visited = set() 
    parent = {} 

    while priority_queue:
        _, curr = heapq.heappop(priority_queue)

        if curr in visited:
            continue  

        visited.add(curr)

        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = parent.get(curr)
            return path[::-1]

        if not any(neighbor not in visited for neighbor in graph[curr]):
            break  

        neighbors = sorted(graph[curr].items(), key=lambda x: heuristic[x[0]])
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                parent[neighbor] = curr

    return None 

graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 4, 'D': 1},
    'B': {'E': 3, 'F': 1},
    'C': {},
    'D': {},
    'E': {'H': 5},
    'F': {'I': 2, 'G': 3},
    'H': {},
    'I': {},
    'G': {}
}

heuristic = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'H': 4, 'I': 9, 'G': 0
}

start_node = 'S'
goal_node = 'G'
path = greedy_search(graph, heuristic, start_node, goal_node)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")