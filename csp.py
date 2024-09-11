# Function to check if the current color assignment is valid
def is_safe(node, color, graph, color_assignment):
    # Check all adjacent nodes (neighbors)
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True

# Backtracking function to solve the map coloring problem
def map_coloring(graph, num_colors, color_assignment, node):
    # If all nodes are assigned a color, return True
    if node == len(graph):
        return True

    # Try different colors for the current node
    for color in range(1, num_colors + 1):
        if is_safe(node, color, graph, color_assignment):
            # Assign color to the node
            color_assignment[node] = color

            # Recursively assign colors to the rest of the nodes
            if map_coloring(graph, num_colors, color_assignment, node + 1):
                return True

            # If assigning the current color doesn't lead to a solution, backtrack
            color_assignment[node] = 0

    return False

# Function to start the map coloring process
def solve_map_coloring(graph, num_colors):
    color_assignment = [0] * len(graph)  # Array to store color assignment for each node

    if not map_coloring(graph, num_colors, color_assignment, 0):
        return "No solution found"
    
    # Return the color assignment for each node
    return color_assignment

# Function to get user input
def get_user_input():
    # Get the number of nodes (regions)
    num_nodes = int(input("Enter the number of nodes (regions): "))
    
    graph = [[] for _ in range(num_nodes)]
    
    # Get the adjacency list from the user
    print("Enter the adjacency list:")
    for i in range(num_nodes):
        neighbors = input(f"Enter neighbors for node {i} (space-separated): ").split()
        graph[i] = [int(neighbor) for neighbor in neighbors]

    # Get the number of colors
    num_colors = int(input("Enter the number of colors: "))

    return graph, num_colors

# Main function to execute the map coloring
if __name__ == "__main__":
    graph, num_colors = get_user_input()
    solution = solve_map_coloring(graph, num_colors)

    if isinstance(solution, str):
        print(solution)
    else:
        print("Solution found! Color assignments:", solution)
