import math

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:  # Leaf nodes are at depth 3
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Explore the two child nodes
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Explore the two child nodes
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Get user input for leaf node values
def get_user_input():
    num_leaf_nodes = 8  # Since it's a binary tree of depth 3, there are 2^3 = 8 leaf nodes
    print(f"Enter {num_leaf_nodes} values for the leaf nodes:")
    values = []
    for i in range(num_leaf_nodes):
        value = int(input(f"Leaf node {i + 1} value: "))
        values.append(value)
    return values

# Main function to start alpha-beta pruning
if __name__ == "__main__":
    # Get user input for leaf node values
    values = get_user_input()

    # Initialize alpha to negative infinity and beta to positive infinity
    alpha = -math.inf
    beta = math.inf

    # Start the algorithm: depth = 0, node_index = 0, maximizing_player = True
    optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta)

    # Output the result
    print("Optimal value:", optimal_value)
