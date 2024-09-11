def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result:  
                return result
    return None
def get_user_input():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the adjacency list for each node:")
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter neighbors of node {node} (space-separated): ").split()
        graph[node] = neighbors
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    return graph, start_node, goal_node
if __name__ == "__main__":
    graph, start_node, goal_node = get_user_input()
    path = dfs(graph, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
