import heapq

g = {
    'A': {'B': 10, 'C': 15},
    'B': {'D': 12, 'F': 15},
    'C': {'E': 10},
    'D': {'E': 2, 'F': 1},
    'F': {'E': 5},
    'E': {}
}

def dijkstra(g, src, tgt):
    pq = [(0, src)]
    dist = {n: float('inf') for n in g}
    dist[src] = 0
    par = {}

    while pq:
        current_d, c_node = heapq.heappop(pq)

        if c_node == tgt:
            break

        if current_d > dist[c_node]:
            continue

        for neighbor, w in g[c_node].items():
            new_d = current_d + w
            if new_d < dist[neighbor]:
                dist[neighbor] = new_d
                par[neighbor] = c_node
                heapq.heappush(pq, (new_d, neighbor))

    path = []
    n = tgt
    while n in par:
        path.append(n)
        n = par[n]
    path.append(src)
    path.reverse()

    return path, dist[tgt]

src, tgt = 'A', 'E'
path, cost = dijkstra(g, src, tgt)
print(f"Shortest path: {' → '.join(path)}")
print(f"Cost: {cost}")
