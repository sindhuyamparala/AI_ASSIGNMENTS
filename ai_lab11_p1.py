import sys

def minimax(depth, node_index, is_max, values, alpha, beta):
    if depth == 2:
        return values[node_index]
    
    if is_max:
        best = -sys.maxsize
        for a in range(3):
            val = minimax(depth + 1, node_index * 3 + a, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            if beta <= alpha:
                break
        return best
    
    else:
        best = sys.maxsize
        for a in range(3):
            val = minimax(depth + 1, node_index * 3 + a, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            if beta <= alpha:
                break
        return best


def optimal_path():
    nodes = ["B1", "B2", "B3"]
    children = [
        ["C1", "C2", "C3"],
        ["C4", "C5", "C6"],
        ["C7", "C8", "C9"]
    ]

    values = [12, 10, 3, 5, 8, 10, 11, 2, 12]
    
    best_score_A = -sys.maxsize
    best_score_B = -sys.maxsize
    best_node = ""
    best_child = ""
    
    for a in range(3):
        score_B = minimax(1, a, False, values, -sys.maxsize, sys.maxsize)
        print(f"Value Of {nodes[a]}: {score_B}")
        
        if score_B > best_score_B:
            best_score_B = score_B
            best_node = nodes[a]
            
            min_score = sys.maxsize
            best_child_index = -1
            for b in range(3):
                child_index = a * 3 + b
                if values[child_index] < min_score:
                    min_score = values[child_index]
                    best_child_index = b
            
            best_child = children[a][best_child_index]
    
    best_score_A = best_score_B
    print(f"Value from A: {best_score_A}")
    print(f"\nOptimal path: A → {best_node} → {best_child}")
    print(f"Optimal Value: {best_score_A}")

optimal_path()
