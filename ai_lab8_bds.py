


from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E', 'F'],
    'F': ['E'],
    'E': []
}

def bidi_search(src, tgt):
    if src == tgt:
        return [src]

    q_src = deque([src])
    q_tgt = deque([tgt])
    vis_src = {src: None}
    vis_tgt = {tgt: None}

    while q_src and q_tgt:
        meet = expand(graph, q_src, vis_src, vis_tgt)
        if meet:
            return build_path(meet, vis_src, vis_tgt)

        meet = expand(reverse(graph), q_tgt, vis_tgt, vis_src)
        if meet:
            return build_path(meet, vis_src, vis_tgt)

    return None

def expand(g, q, vis_this, vis_other):
    curr = q.popleft()
    for nbr in g.get(curr, []):
        if nbr not in vis_this:
            vis_this[nbr] = curr
            q.append(nbr)
            if nbr in vis_other:
                return nbr
    return None

def reverse(g):
    rev = {n: [] for n in g}
    for src in g:
        for dst in g[src]:
            rev[dst].append(src)
    return rev

def build_path(meet, vis_s, vis_t):
    path = []
    node = meet
    while node:
        path.append(node)
        node = vis_s[node]
    path.reverse()

    node = vis_t[meet]
    while node:
        path.append(node)
        node = vis_t[node]

    return path

path = bidi_search('A', 'E')
if path:
    print(f"Bi-Directional Path: {' -> '.join(path)}")
else:
    print("No path found.")
