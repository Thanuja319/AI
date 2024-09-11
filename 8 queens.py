def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False
def print_solution(board, n):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()
def solve_n_queens_problem(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist for", n, "queens.")
    else:
        print_solution(board, n)
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solve_n_queens_problem(n)
