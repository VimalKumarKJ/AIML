def min_max(depth, node_index, is_maximizing_player, values):
    if depth == 3:
        return values[node_index]
    
    if is_maximizing_player:
        best_value = float('-inf')
        for i in range(2):
            value = min_max(depth + 1, node_index * 2 + i, False, values)
            best_value = max(best_value, value)
        return best_value
    
    else:
        best_value = float('inf')
        for i in range(2):
            value = min_max(depth + 1, node_index * 2 + i, True, values)
            best_value = min(best_value, value)
        return best_value
    
if __name__  == "__main__":
    values = [1, 5, 12, 9, 2, 5, 13, 6]
    print("The optimal value is:", min_max(0, 0, True, values))