def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()
def move(board, direction):
    empty_i, empty_j = find_empty(board)
    if direction == 'up' and empty_i > 0:
        board[empty_i][empty_j], board[empty_i - 1][empty_j] = board[empty_i - 1][empty_j], board[empty_i][empty_j]
    elif direction == 'down' and empty_i < 2:
        board[empty_i][empty_j], board[empty_i + 1][empty_j] = board[empty_i + 1][empty_j], board[empty_i][empty_j]
    elif direction == 'left' and empty_j > 0:
        board[empty_i][empty_j], board[empty_i][empty_j - 1] = board[empty_i][empty_j - 1], board[empty_i][empty_j]
    elif direction == 'right' and empty_j < 2:
        board[empty_i][empty_j], board[empty_i][empty_j + 1] = board[empty_i][empty_j + 1], board[empty_i][empty_j]
    return board
def find_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
initial_state = []
print("Enter the initial state (use 0 for the empty space):")
for i in range(3):
    row = list(map(int, input(f"Enter row {i + 1} (e.g., '1 2 3'): ").split()))
    initial_state.append(row)
print("\nInitial State:")
print_board(initial_state)
direction = input("Enter the move direction ('up', 'down', 'left', 'right'): ").lower()
print(f"\nMove '{direction}':")
print_board(move(initial_state, direction))
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
print("Goal State:")
print_board(goal_state)
