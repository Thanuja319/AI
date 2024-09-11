import itertools

def calculate_distance(cities, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += cities[path[i]][path[i+1]]
    total_distance += cities[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def tsp_bruteforce(cities):
    n = len(cities)
    all_permutations = itertools.permutations(range(n))
    min_distance = float('inf')
    best_path = None
    
    for path in all_permutations:
        distance = calculate_distance(cities, path)
        if distance < min_distance:
            min_distance = distance
            best_path = path
    
    return best_path, min_distance

def get_user_input():
    # Get the number of cities
    num_cities = int(input("Enter the number of cities: "))
    
    cities = []
    print("Enter the distance matrix row by row:")
    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances from city {i} (space-separated): ").split()))
        if len(row) != num_cities:
            raise ValueError("The number of distances entered does not match the number of cities.")
        cities.append(row)
    
    return cities

if __name__ == "__main__":
    cities = get_user_input()
    
    # Solve the TSP
    best_path, min_distance = tsp_bruteforce(cities)
    
    # Output the result
    print("Best path:", best_path)
    print("Minimum distance:", min_distance)
