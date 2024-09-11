from collections import deque
def water_jug_solver(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])
    steps = []
    while queue:
        (jug1, jug2) = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        steps.append((jug1, jug2))
        if jug1 == target or jug2 == target:
            return steps
        queue.append((jug1_capacity, jug2))
        queue.append((jug1, jug2_capacity))
        queue.append((0, jug2))
        queue.append((jug1, 0))
        pour_into_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour_into_jug2, jug2 + pour_into_jug2))
        pour_into_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour_into_jug1, jug2 - pour_into_jug1))
    return None
def print_solution(steps):
    print("Steps to reach the target:")
    for step in steps:
        print(f"Jug 1: {step[0]} liters, Jug 2: {step[1]} liters")
if __name__ == "__main__":
    jug1_capacity = int(input("Enter the capacity of Jug 1 (in liters): "))
    jug2_capacity = int(input("Enter the capacity of Jug 2 (in liters): "))
    target = int(input("Enter the target amount of water (in liters): "))
    solution = water_jug_solver(jug1_capacity, jug2_capacity, target)
    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
