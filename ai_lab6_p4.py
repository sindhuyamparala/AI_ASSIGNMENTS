def has_cycle(g):
    vis = set()
    stack = set()

    def dfs(n):
        if n not in vis:
            vis.add(n)
            stack.add(n)

            for nb in g[n]:
                if nb not in vis and dfs(nb):
                    return True
                elif nb in stack:
                    return True

            stack.discard(n)  
        return False

    for n in g:
        if dfs(n):
            return True
    return False


g = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': [],
    'F': ['E']
}

res = has_cycle(g)
print(f"Cycle detected: {res}")