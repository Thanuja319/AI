from sys import maxsize
from itertools import permutations


# Function to solve the Travelling Salesman Problem
def travellingSalesmanProblem(graph, s):
    V = len(graph)
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)

    return min_path


# Function to take input from the user
def input_graph():
    V = int(input("Enter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix (row by row):")
    for i in range(V):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        graph.append(row)

    return graph


# Main function
if __name__ == "__main__":
    graph = input_graph()
    s = int(input("Enter the starting vertex (0 to V-1): "))

    print("Minimum path cost for Travelling Salesman Problem:", travellingSalesmanProblem(graph, s))
