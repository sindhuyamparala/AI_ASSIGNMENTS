def minimax(node, depth, maximizing, path):
    if isinstance(node, int):
        return node, path
    best_path = []
    if maximizing:
        best_value = float('-inf')
        for i, n in enumerate(node):
            value, sub_path = minimax(n, depth + 1, False, path + [f'N{depth*4 + i + 1}'])
            if value > best_value:
                best_value = value
                best_path = sub_path
    else:
        best_value = float('inf')
        for i, n in enumerate(node):
            value, sub_path = minimax(n, depth + 1, True, path + [f'N{depth*4 + i + 1}'])
            if value < best_value:
                best_value = value
                best_path = sub_path
    return best_value, best_path
tree = [
     [
        [[5, -1, 4, 3], [2, -5, 9, 8]],    
        [[6, 1, -4, 2], [4, 7, 3, -3]] 
     ] 
 ]   
optimal_value, optimal_path = minimax(tree, 0, True, ['Root'])
print(f"Optimal Value:{optimal_value}")
print(f"Optimal Path:- {' -> '.join(optimal_path)}")