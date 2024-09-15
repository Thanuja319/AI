def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node6]:
            dfs(visited, graph, neighbour)


# Function to take input from the user
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        node = input(f"Enter node {i + 1}: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors

    return graph


# Main function
if __name__ == "__main__":
    visited = set()
    graph = input_graph()

    start_node = input("Enter the starting node for DFS: ")

    print("Following is the Depth-First Search")
    dfs(visited, graph, start_node)
