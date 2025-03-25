def dfs(g, n, vis=None):
    if vis is None:
        vis = set()
    if n not in vis:
        vis.add(n)
        print(n, end=' → ')
        for nb in g[n]:
            dfs(g, nb, vis)

g = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': [],
    'F': ['E']
}

print("DFS Traversal: ", end="")
dfs(g, 'A')
print("End")
