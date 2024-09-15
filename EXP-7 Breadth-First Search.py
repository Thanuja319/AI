# Function to input the graph from the user
def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))

    for i in range(n):
        node = input(f"Enter node {i + 1}: ")
        neighbours = input(f"Enter the neighbors of {node} (space-separated): ").split()
        graph[node] = neighbours

    return graph


visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Taking graph and start node as input from the user
graph = input_graph()
start_node = input("Enter the start node for BFS: ")

print("Following is the Breadth-First Search")
bfs(visited, graph, start_node)
