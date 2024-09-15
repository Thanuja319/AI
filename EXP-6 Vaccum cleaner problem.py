import random

def display(room):
    for row in room:
        print(row)

# Taking input for the matrix dimensions
rows = int(input("Enter the number of rows in the room: "))
cols = int(input("Enter the number of columns in the room: "))

# Initializing the room with all rooms dirty (1)
room = []
for i in range(rows):
    room.append([1] * cols)

print("All the rooms are dirty")
display(room)

# Randomly dirty the rooms
for x in range(rows):
    for y in range(cols):
        room[x][y] = random.choice([0, 1])

print("Before cleaning the room, I detected all of these random dirts")
display(room)

# Clean the room
z = 0
for x in range(rows):
    for y in range(cols):
        if room[x][y] == 1:
            print(f"Vacuuming at location ({x}, {y})")
            room[x][y] = 0
            print(f"Cleaned location ({x}, {y})")
            z += 1

# Calculate performance
pro = (100 - ((z / (rows * cols)) * 100))
print("Room is clean now. Thanks for using the vacuum cleaner!")
display(room)
print(f'Performance = {pro:.2f}%')
