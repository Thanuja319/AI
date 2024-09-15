import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def astar_search(start, goal, heuristic_func, neighbors_func):
    open_set = []
    closed_set = set()
    start_node = Node(state=start, cost=0, heuristic=heuristic_func(start))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(current_node.state)

        for neighbor in neighbors_func(current_node.state):
            if neighbor in closed_set:
                continue
            tentative_cost = current_node.cost + 1
            neighbor_node = Node(state=neighbor, parent=current_node, cost=tentative_cost, heuristic=heuristic_func(neighbor))

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)
            else:
                for node in open_set:
                    if node.state == neighbor and node.total_cost > neighbor_node.total_cost:
                        open_set.remove(node)
                        heapq.heappush(open_set, neighbor_node)
    return None

# Heuristic Function
def heuristic(state):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# Function to find valid neighbors
def neighbors(state, grid_size, obstacles):
    x, y = state
    possible_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    valid_neighbors = [(x, y) for x, y in possible_neighbors if 0 <= x < grid_size and 0 <= y < grid_size and (x, y) not in obstacles]
    return valid_neighbors

# Function to take user input
def input_data():
    grid_size = int(input("Enter grid size (e.g., 10 for a 10x10 grid): "))

    start_x, start_y = map(int, input("Enter starting coordinates (e.g., 0 0): ").split())
    start = (start_x, start_y)

    goal_x, goal_y = map(int, input("Enter goal coordinates (e.g., 9 9): ").split())
    global goal
    goal = (goal_x, goal_y)

    obstacles = []
    obstacle_count = int(input("Enter number of obstacles: "))
    for _ in range(obstacle_count):
        obs_x, obs_y = map(int, input("Enter obstacle coordinates (e.g., 3 4): ").split())
        obstacles.append((obs_x, obs_y))

    return grid_size, start, goal, obstacles

if __name__ == "__main__":
    grid_size, start, goal, obstacles = input_data()

    # Call the A* search algorithm
    path = astar_search(start, goal, heuristic, lambda state: neighbors(state, grid_size, obstacles))

    if path:
        print("Path found:", path)
    else:
        print("No path found")
