import random

class VacuumCleaner:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = self.create_grid()
        self.position = [0, 0]  

    def create_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def display_grid(self):
        for row in self.grid:
            print(row)
        print()

    def clean(self):
        if self.grid[self.position[0]][self.position[1]] == 1:
            print(f"Cleaning dirt at position {self.position}")
            self.grid[self.position[0]][self.position[1]] = 0
        else:
            print(f"No dirt at position {self.position}")

    def move(self, direction):
        if direction == 'up' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'down' and self.position[0] < self.grid_size - 1:
            self.position[0] += 1
        elif direction == 'left' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'right' and self.position[1] < self.grid_size - 1:
            self.position[1] += 1
        else:
            print("Invalid move")

    def is_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        self.display_grid()
        while not self.is_clean():
            self.clean()
            # Simple movement strategy: move right until end, then down, then left, etc.
            if self.position[1] < self.grid_size - 1:
                self.move('right')
            elif self.position[0] < self.grid_size - 1:
                self.move('down')
                while self.position[1] > 0:
                    self.move('left')
                if self.position[0] < self.grid_size - 1:
                    self.move('down')
            self.display_grid()
        print("Cleaning complete!")

def get_user_input():
    grid_size = int(input("Enter the grid size (e.g., 2 for a 2x2 grid): "))
    return grid_size

if __name__ == "__main__":
    grid_size = get_user_input()
    vacuum = VacuumCleaner(grid_size=grid_size)
    vacuum.run()
