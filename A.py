import heapq
def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path
def a_star_algorithm(start, goal, graph, h):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    came_from = {}

    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

# Function to get user input
def get_user_input():
    graph = {}
    h = {}
    
    # Get the number of nodes
    num_nodes = int(input("Enter the number of nodes: "))

    # Get the adjacency list
    print("Enter the adjacency list for each node:")
    for i in range(num_nodes):
        node = input(f"Node {i}: ")
        neighbors = input(f"Neighbors of node {node} (format: neighbor1,cost1 neighbor2,cost2 ...): ")
        neighbor_list = [tuple(map(int, n.split(','))) for n in neighbors.split()]
        graph[node] = neighbor_list

    # Get heuristic values
    print("Enter heuristic values for each node:")
    for i in range(num_nodes):
        node = input(f"Node {i}: ")
        heuristic = int(input(f"Heuristic value for node {node}: "))
        h[node] = heuristic

    # Get start and goal nodes
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    return start_node, goal_node, graph, h

# Main function to execute the A* algorithm with user input
if __name__ == "__main__":
    start_node, goal_node, graph, h = get_user_input()
    path = a_star_algorithm(start_node, goal_node, graph, h)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
