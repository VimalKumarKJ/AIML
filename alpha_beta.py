def alpha_beta(depth, node_index, alpha, beta, is_maximising_player, values):
    if depth == 3:
        return values[node_index]
    
    if is_maximising_player:
        best_value = float('-inf')
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta, False, values)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break;
        return best_value
    else:
        best_value = float('inf')
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta, True, values)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta >= alpha:
                break;
        return best_value
if __name__ == "__main__":
    values = [1, 5, 12, 9, 2, 5, 13, 6]
    print("The optimal value is: ", alpha_beta(0, 0, float('-inf'), float('inf'), True, values))
    

    