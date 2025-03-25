from collections import deque

def bfs(g, src):
    vis = set()
    q = deque([src])
    order = []

    while q:
        n = q.popleft()
        if n not in vis:
            vis.add(n)
            order.append(n)
            for nb in g[n]:
                if nb not in vis:
                    q.append(nb)

    return order

g = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': [],
    'F': ['E']
}

src = 'A'
res = bfs(g, src)
print(f"BFS Traversal: {' → '.join(res)}")
